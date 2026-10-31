#!/usr/bin/env python3
"""
Automated Open Source Contributions updater for Aditya Malkar's Profile README.
Fetches public pull requests across external repositories and rewrites the section
between the contributions comment tags: a summary line and a grid with one card per
project, showing merged and open tags for its pull requests.
"""

import os
import re
import html
import json
import urllib.parse
import urllib.request
import subprocess
from collections import defaultdict

USER = 'adimalkar'
# Pull requests outside these owners count as open source contributions.
EXCLUDED_OWNERS = ('adimalkar', 'hiringfleet')

# One short line per repository, kept to about 50 characters so it fits on one line of its
# card. Repositories without an entry fall back to the title of their latest pull request.
CURATED_IMPACTS = {
    'kornia/kornia': 'Augmentation fixes; revived LoFTR CPU tests',
    'fivetran/great_expectations': 'Infinite `Decimal` serialization; typed test modules',
    'sqlfluff/sqlfluff': 'Snowflake `ALERT` grammar; T-SQL reflow alignment',
    'Arize-ai/phoenix': 'Kept Anthropic/Bedrock tool choice and `strict`',
    'microsoft/PyRIT': 'Non-ASCII words in the PUZZLED keyword masker',
    'mlc-ai/xgrammar': 'JSON Schema references through array indices',
    'NVIDIA/numba-cuda-mlir': 'Float-to-bool conversion in the MLIR lowering',
    'NousResearch/hermes-agent': 'Show saved working directories in session lists',
    'browser-use/browser-use': 'Accept optional types on special action params',
    'vllm-project/vllm': 'Original context length for mRoPE YaRN correction',
    'crewAIInc/crewAI': 'Fail when an expected metric has no score',
    'stanfordnlp/dspy': 'Reject the reserved `trajectory` output in ReAct',
    'microsoft/onnxruntime': 'Keep the producer edge in `DivMulFusion`',
}

DISPLAY_NAMES = {
    'NVIDIA/numba-cuda-mlir': 'numba-cuda-mlir',
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
MAX_IMPACT_CHARS = 50

STATE_COLORS = {'MERGED': '8957e5', 'OPEN': '238636'}

CARDS_PER_ROW = 2

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
    # The cards are raw HTML, where markdown isn't parsed: escape, then turn `code` into <code>.
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', html.escape(text))

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
    return f'<a href="{url}"><img src="{src}" alt="{label} {state.lower()}"/></a>'

def state_tags(repo_name, prs):
    """One tag per state: the pull request itself, or a count that links to the list."""
    tags = []
    for state in ('MERGED', 'OPEN'):
        matching = [p for p in prs if p['state'] == state]
        if len(matching) == 1:
            tags.append(state_tag(f"#{matching[0]['number']}", state, matching[0]['url']))
        elif matching:
            qualifier = 'is:merged' if state == 'MERGED' else 'is:open'
            tags.append(state_tag(f"{len(matching)} PRs", state, search_url(f'{qualifier} repo:{repo_name}')))
    return ' '.join(tags)

def impact_for(repo_name, prs):
    impact = CURATED_IMPACTS.get(repo_name)
    if not impact:
        latest = max(prs, key=lambda p: p['createdAt'])
        impact = clean_pr_title(latest['title'])
        if len(impact) > MAX_IMPACT_CHARS:
            impact = impact[:MAX_IMPACT_CHARS - 1].rstrip() + '…'
    return inline_html(impact)

def build_section(nodes):
    repos = defaultdict(list)
    for pr in nodes:
        repo = pr.get('repository')
        if repo and not repo.get('isPrivate') and pr['state'] in ('OPEN', 'MERGED'):
            repos[repo['nameWithOwner']].append(pr)

    def merged_count(prs):
        return sum(p['state'] == 'MERGED' for p in prs)

    def stars(prs):
        return prs[0]['repository']['stargazerCount']

    total_merged = sum(merged_count(prs) for prs in repos.values())
    total_open = sum(len(prs) for prs in repos.values()) - total_merged
    lines = [
        f"**{total_merged} merged** and **{total_open} open** pull requests across {len(repos)} projects — "
        "fixes and features in ML infrastructure, compilers, agent frameworks, and evaluation tooling.",
        "",
    ]

    # Projects with merged work first, most merged first; then the larger project. A pull
    # request that merges moves its project up on the next run.
    cards = []
    for repo_name, prs in sorted(repos.items(), key=lambda item: (-merged_count(item[1]), -stars(item[1]))):
        disp_name = html.escape(DISPLAY_NAMES.get(repo_name, repo_name.split('/')[1]))
        cards.append(
            f'<td width="50%"><b><a href="https://github.com/{repo_name}">{disp_name}</a></b>&nbsp; '
            f'{state_tags(repo_name, prs)}<br>'
            f'<sub>★ {format_stars(stars(prs))} · {impact_for(repo_name, prs)}</sub></td>'
        )

    # Two cards per row. The table is one HTML block, so it must not contain a blank line.
    lines.append("<table>")
    for i in range(0, len(cards), CARDS_PER_ROW):
        row = cards[i:i + CARDS_PER_ROW]
        row += ['<td width="50%"></td>'] * (CARDS_PER_ROW - len(row))
        lines += ["<tr>", *row, "</tr>"]
    lines.append("</table>")

    lines += [
        "",
        f'<p align="center"><a href="{search_url("is:merged")}"><img src="https://img.shields.io/badge/GitHub-All_{total_merged}_merged_open_source_PRs-238636?style=for-the-badge&logo=github&logoColor=white" alt="All merged open source PRs" /></a></p>',
    ]
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
    section = build_section(nodes)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    readme_path = os.path.join(repo_root, 'README.md')

    print(f"Updating {readme_path}...")
    changed = update_readme(section, readme_path)
    if changed:
        print("README.md updated with latest contributions!")
    else:
        print("README.md is already up to date.")

if __name__ == '__main__':
    main()
