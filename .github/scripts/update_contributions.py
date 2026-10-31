#!/usr/bin/env python3
"""
Automated Open Source Contributions updater for Aditya Malkar's Profile README.
Fetches public pull requests across external repositories and rewrites the section
between the contributions comment tags: a summary line, the organizations contributed to,
and a grid with one card per project, showing merged and open tags for its pull requests.
"""

import os
import re
import html
import json
import base64
import hashlib
import urllib.parse
import urllib.request
import subprocess
from collections import defaultdict

USER = 'adimalkar'
# Pull requests outside these owners count as open source contributions.
EXCLUDED_OWNERS = ('adimalkar', 'hiringfleet')

# One line per repository, about 80 characters, so it fills its card in two lines at most.
# Repositories without an entry fall back to the title of their latest pull request.
CURATED_IMPACTS = {
    'kornia/kornia': 'Fixed PatchMix, RandomResizedCrop and rank errors; revived LoFTR CPU tests',
    'fivetran/great_expectations': 'Serialized infinite `Decimal`s instead of raising; type-checked 8 excluded test modules',
    'sqlfluff/sqlfluff': 'Snowflake `ALERT` DDL grammar; reflow alignment for leading-comma T-SQL',
    'Arize-ai/phoenix': 'Kept Anthropic and Bedrock tool choice and `strict` settings in the playground and evals',
    'microsoft/PyRIT': 'Let the PUZZLED keyword masker select words with non-ASCII letters',
    'mlc-ai/xgrammar': 'Resolved JSON Schema references through array indices for structured generation',
    'NVIDIA/numba-cuda-mlir': 'Float-to-bool conversion compares against zero instead of truncating',
    'NousResearch/hermes-agent': 'Show saved working directories in CLI session lists',
    'browser-use/browser-use': 'Accept `X | None` annotations on special action parameters',
    'vllm-project/vllm': 'Use the original context length for the mRoPE YaRN correction range',
    'crewAIInc/crewAI': 'Fail an evaluation when an expected metric has no score instead of passing it',
    'stanfordnlp/dspy': 'Reject the reserved `trajectory` output name in ReAct at construction time',
    'microsoft/onnxruntime': 'Reconnect the producer edge when `DivMulFusion` substitutes the Mul\'s input',
}

DISPLAY_NAMES = {
    'NVIDIA/numba-cuda-mlir': 'numba-cuda-mlir',
    'fivetran/great_expectations': 'Great Expectations',
    'microsoft/onnxruntime': 'ONNX Runtime',
    'microsoft/PyRIT': 'PyRIT',
    'stanfordnlp/dspy': 'DSPy',
    'Arize-ai/phoenix': 'Arize Phoenix',
    'crewAIInc/crewAI': 'CrewAI',
    'mlc-ai/xgrammar': 'xgrammar',
    'langchain-ai/langchainjs': 'LangChain.js',
    'vllm-project/vllm': 'vLLM',
}

# Fallback descriptions are cut to this many characters.
MAX_IMPACT_CHARS = 90

STATE_COLORS = {'MERGED': '8957e5', 'OPEN': '238636'}

CARDS_PER_ROW = 2
CHIPS_PER_ROW = 4

def get_token():
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token:
        try:
            token = subprocess.check_output(['gh', 'auth', 'token'], text=True).strip()
        except Exception:
            token = None
    return token

def search_qualifiers():
    return f"is:pr author:{USER} " + ' '.join(f"-user:{owner}" for owner in EXCLUDED_OWNERS)

def search_url(extra=''):
    query = f"{search_qualifiers()} {extra}".strip()
    return 'https://github.com/pulls?q=' + urllib.parse.quote_plus(query)

def fetch_prs(token):
    query = """
    query($q: String!) {
      search(query: $q, type: ISSUE, first: 100) {
        nodes {
          ... on PullRequest {
            number
            title
            state
            url
            createdAt
            mergedAt
            repository {
              nameWithOwner
              stargazerCount
              isPrivate
              owner {
                login
                avatarUrl
              }
            }
          }
        }
      }
    }
    """
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Profile-Readme-Updater'
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'

    req = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': query, 'variables': {'q': search_qualifiers()}}).encode('utf-8'),
        headers=headers
    )

    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))

    if 'errors' in res:
        raise RuntimeError(f"GraphQL error: {res['errors']}")

    return res['data']['search']['nodes']

def clean_pr_title(title):
    # Remove conventional commit prefixes like feat:, fix(scope):, [BUGFIX], etc.
    cleaned = title
    while True:
        stripped = re.sub(r'^(?:\[[^\]]+\]|\b(?:feat|fix|perf|chore|docs|refactor|ci|test)(?:\([^)]+\))?:)\s*', '', cleaned, flags=re.I)
        if stripped == cleaned:
            break
        cleaned = stripped
    cleaned = cleaned.strip()
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned

def inline_html(text):
    # The cards are raw HTML, where markdown isn't parsed. Plain text reads cleaner than
    # code spans in a card, so backticks are dropped.
    return html.escape(text.replace('`', ''))

def format_stars(stars):
    if stars >= 1000:
        thousands = stars / 1000
        return f"{thousands:.0f}k" if thousands >= 100 else f"{thousands:.1f}k".replace('.0k', 'k')
    return str(stars)

def badge_text(text):
    # shields.io static badges read `-` and `_` as separators.
    return urllib.parse.quote(text.replace('-', '--').replace('_', '__'))

def state_tag(label, state, url):
    color = STATE_COLORS[state]
    src = f"https://img.shields.io/badge/{badge_text(label)}-{state.lower()}-{color}?style=flat-square"
    # align="right" floats the tag to the card's right edge, so tags line up down the grid.
    return f'<a href="{url}"><img align="right" src="{src}" alt="{label} {state.lower()}"/></a>'

def state_tags(repo_name, prs):
    """One tag per state: the pull request itself, or a count that links to the list.

    Right floats stack from the edge inward, so the open tag comes first to end up rightmost.
    """
    tags = []
    for state in ('OPEN', 'MERGED'):
        matching = [p for p in prs if p['state'] == state]
        if len(matching) == 1:
            tags.append(state_tag(f"#{matching[0]['number']}", state, matching[0]['url']))
        elif matching:
            qualifier = 'is:merged' if state == 'MERGED' else 'is:open'
            tags.append(state_tag(f"{len(matching)} PRs", state, search_url(f'{qualifier} repo:{repo_name}')))
    return ''.join(tags)

def impact_for(repo_name, prs):
    impact = CURATED_IMPACTS.get(repo_name)
    if not impact:
        latest = max(prs, key=lambda p: p['createdAt'])
        impact = clean_pr_title(latest['title'])
        if len(impact) > MAX_IMPACT_CHARS:
            impact = impact[:MAX_IMPACT_CHARS - 1].rstrip() + '…'
    return inline_html(impact)

# Bold Arial advance widths in 1/1000 em, to size each chip to its text.
CHAR_WIDTHS = dict(zip(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@-_.',
    [556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556,
     333, 611, 556, 778, 556, 556, 500, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611,
     833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611] + [556] * 10 + [975, 333, 556, 278],
))

CHIP_SVG = """<!-- {key} -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="32" viewBox="0 0 {width} 32">
<style>
.bg{{fill:#f6f8fa;stroke:#d0d7de}}.name{{fill:#1f2328}}
@media (prefers-color-scheme: dark){{.bg{{fill:#161b22;stroke:#30363d}}.name{{fill:#e6edf3}}}}
</style>
<clipPath id="avatar"><rect x="8" y="6" width="20" height="20" rx="4"/></clipPath>
<rect class="bg" x="0.5" y="0.5" width="{rect_width}" height="31" rx="6"/>
<image x="8" y="6" width="20" height="20" clip-path="url(#avatar)" xlink:href="{avatar}"/>
<text class="name" x="36" y="21" textLength="{text_width}" lengthAdjust="spacingAndGlyphs" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif" font-size="14" font-weight="600">{label}</text>
</svg>
"""

def chip_text_width(login):
    return round(sum(CHAR_WIDTHS.get(c, 611) for c in f'@{login}') * 14 / 1000)

def chip_key(avatar_url, width):
    """What a chip is drawn from. The avatar CDN doesn't always return identical bytes for
    the same avatar, so a chip is redrawn only when this changes, not on every run."""
    template = hashlib.sha256(CHIP_SVG.encode()).hexdigest()[:12]
    return f'avatar={avatar_url} width={width} template={template}'

def chip_svg(login, avatar_bytes, content_type, width, key):
    label = f'@{login}'
    text_width = chip_text_width(login)
    avatar = f'data:{content_type};base64,{base64.b64encode(avatar_bytes).decode()}'
    return CHIP_SVG.format(key=key, width=width, rect_width=width - 1, text_width=text_width,
                           avatar=avatar, label=html.escape(label))

def fetch_avatar(avatar_url):
    separator = '&' if '?' in avatar_url else '?'
    req = urllib.request.Request(f'{avatar_url}{separator}s=40', headers={'User-Agent': 'Profile-Readme-Updater'})
    with urllib.request.urlopen(req) as resp:
        return resp.read(), resp.headers.get_content_type()

def org_chips(repos, sort_key, chip_dir):
    """One chip image per organization, linking to the pull requests made there.

    Each chip is a single image, so it never wraps between its avatar and its name, and it
    is drawn from GitHub's own data rather than by a third-party badge service.
    """
    owners = {}
    for repo_name, prs in sorted(repos.items(), key=sort_key):
        owner = prs[0]['repository']['owner']
        owners.setdefault(owner['login'], owner['avatarUrl'])

    # Every chip is as wide as the widest, so the rows form a grid with aligned columns.
    width = 36 + max(chip_text_width(login) for login in owners) + 12
    os.makedirs(chip_dir, exist_ok=True)
    chips = []
    for login, avatar_url in owners.items():
        filename = f'{login.lower()}.svg'
        path = os.path.join(chip_dir, filename)
        key = chip_key(avatar_url, width)
        if not (os.path.exists(path) and open(path, encoding='utf-8').readline().strip() == f'<!-- {key} -->'):
            with open(path, 'w', encoding='utf-8') as f:
                f.write(chip_svg(login, *fetch_avatar(avatar_url), width, key))
        chips.append(
            f'<a href="{search_url(f"user:{login}")}">'
            f'<img src="{os.path.basename(chip_dir)}/{filename}" height="32" alt="@{html.escape(login)}"/></a>'
        )
    # Drop the chips of organizations no longer listed.
    keep = {f'{login.lower()}.svg' for login in owners}
    for stale in set(os.listdir(chip_dir)) - keep:
        os.remove(os.path.join(chip_dir, stale))
    rows = [' '.join(chips[i:i + CHIPS_PER_ROW]) for i in range(0, len(chips), CHIPS_PER_ROW)]
    return '<br>'.join(rows)

def build_section(nodes, chip_dir):
    repos = defaultdict(list)
    for pr in nodes:
        repo = pr.get('repository')
        if repo and not repo.get('isPrivate') and pr['state'] in ('OPEN', 'MERGED'):
            repos[repo['nameWithOwner']].append(pr)

    def merged_count(prs):
        return sum(p['state'] == 'MERGED' for p in prs)

    def stars(prs):
        return prs[0]['repository']['stargazerCount']

    # Projects with merged work first, most merged first; then the larger project. A pull
    # request that merges moves its project up on the next run.
    def sort_key(item):
        return (-merged_count(item[1]), -stars(item[1]))

    total_merged = sum(merged_count(prs) for prs in repos.values())
    total_open = sum(len(prs) for prs in repos.values()) - total_merged
    owners = {prs[0]['repository']['owner']['login'] for prs in repos.values()}
    lines = [
        f"**{total_merged} merged** and **{total_open} open** pull requests across {len(repos)} projects "
        f"in {len(owners)} organizations — fixes and features in ML infrastructure, compilers, agent "
        "frameworks, and evaluation tooling.",
        "",
    ]

    cards = []
    for repo_name, prs in sorted(repos.items(), key=sort_key):
        disp_name = html.escape(DISPLAY_NAMES.get(repo_name, repo_name.split('/')[1]))
        cards.append(
            f'<td width="50%" valign="top">{state_tags(repo_name, prs)}'
            f'<b><a href="https://github.com/{repo_name}">{disp_name}</a></b><br>'
            f'★ {format_stars(stars(prs))} · {impact_for(repo_name, prs)}</td>'
        )

    button = (
        f'<a href="{search_url("is:merged")}"><img src="https://img.shields.io/badge/GitHub-All_{total_merged}'
        '_merged_open_source_PRs-238636?style=for-the-badge&logo=github&logoColor=white" '
        'alt="All merged open source PRs" /></a>'
    )
    # An odd card count leaves one cell free; the button fills it instead of a blank cell.
    if len(cards) % CARDS_PER_ROW:
        cards.append(f'<td width="50%" align="center">{button}</td>')
        button = None

    # One bordered block: the organizations, then two cards per row. The table is one HTML
    # block, so it must not contain a blank line.
    lines += [
        "<table>",
        "<tr>",
        f'<td colspan="{CARDS_PER_ROW}" align="center">{org_chips(repos, sort_key, chip_dir)}</td>',
        "</tr>",
    ]
    for i in range(0, len(cards), CARDS_PER_ROW):
        lines += ["<tr>", *cards[i:i + CARDS_PER_ROW], "</tr>"]
    if button:
        lines += ["<tr>", f'<td colspan="{CARDS_PER_ROW}" align="center">{button}</td>', "</tr>"]
    lines.append("</table>")
    return '\n'.join(lines)

def update_readme(section, readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<!-- START_SECTION:contributions -->)(.*?)(<!-- END_SECTION:contributions -->)'
    if not re.search(pattern, content, flags=re.DOTALL):
        raise RuntimeError('README.md has no contributions section markers')
    new_content = re.sub(pattern, lambda m: f'{m.group(1)}\n{section}\n{m.group(3)}', content, flags=re.DOTALL)

    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    token = get_token()
    print("Fetching external PRs from GitHub...")
    nodes = fetch_prs(token)
    print(f"Found {len(nodes)} PRs across external repositories.")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    readme_path = os.path.join(repo_root, 'README.md')
    section = build_section(nodes, os.path.join(repo_root, 'orgs'))

    print(f"Updating {readme_path}...")
    changed = update_readme(section, readme_path)
    if changed:
        print("README.md updated with latest contributions!")
    else:
        print("README.md is already up to date.")

if __name__ == '__main__':
    main()
