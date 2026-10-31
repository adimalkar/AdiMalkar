#!/usr/bin/env python3
"""
Automated Open Source Contributions updater for Aditya Malkar's Profile README.
Fetches public pull requests across external repositories and rewrites the section
between the contributions comment tags: a summary line, a table of merged work, and a
collapsed list of pull requests still in review.
"""

import os
import re
import json
import urllib.parse
import urllib.request
import subprocess
from collections import defaultdict

USER = 'adimalkar'
# Pull requests outside these owners count as open source contributions.
EXCLUDED_OWNERS = ('adimalkar', 'hiringfleet')

# One line per repository on what the merged work did. Repositories without an entry fall
# back to the title of their latest merged pull request.
CURATED_IMPACTS = {
    'NVIDIA/numba-cuda-mlir': 'Fixed float-to-bool conversion in the MLIR lowering by comparing against zero instead of truncating.',
    'kornia/kornia': 'Revived LoFTR CPU accuracy tests; fixed PatchMix bounding boxes, `same_on_batch` pairing and input-rank errors across augmentations.',
    'Arize-ai/phoenix': 'Fixed playground/evaluator clients silently dropping Anthropic & Bedrock tool-`choice` and `strict` configurations prior to dispatch.',
    'fivetran/great_expectations': 'Resolved 36 mypy errors across 8 excluded integration test modules; serialized infinite `Decimal`s instead of raising.',
    'sqlfluff/sqlfluff': 'Added full AST grammar for Snowflake `CREATE/ALTER/DROP ALERT` DDL; fixed reflow alignment for leading-comma T-SQL.',
    'microsoft/onnxruntime': 'Reconnected producer edge in the graph optimizer when `DivMulFusion` substitutes Mul\'s input.',
    'microsoft/PyRIT': 'Let the PUZZLED keyword masker select words with non-ASCII letters.',
    'stanfordnlp/dspy': 'Rejects reserved `trajectory` as an output field in ReAct — surfaces collision at construction instead of mid-run after billed LM calls.',
    'crewAIInc/crewAI': 'Explicitly fails when expected evaluation metric has no score instead of silently propagating corrupted agent benchmark results.',
    'mlc-ai/xgrammar': 'Resolved JSON Schema references through array indices for grammar-guided LLM structured output generation.'
}

DISPLAY_NAMES = {
    'NVIDIA/numba-cuda-mlir': 'NVIDIA numba-cuda-mlir',
    'microsoft/onnxruntime': 'Microsoft ONNX Runtime',
    'microsoft/PyRIT': 'Microsoft PyRIT',
    'stanfordnlp/dspy': 'Stanford DSPy',
    'Arize-ai/phoenix': 'Arize Phoenix',
    'fivetran/great_expectations': 'great_expectations',
    'kornia/kornia': 'kornia',
    'sqlfluff/sqlfluff': 'sqlfluff',
    'crewAIInc/crewAI': 'CrewAI',
    'mlc-ai/xgrammar': 'MLC-AI xgrammar',
    'langchain-ai/langchainjs': 'LangChain.js',
    'vllm-project/vllm': 'vLLM',
    'NousResearch/hermes-agent': 'hermes-agent',
    'browser-use/browser-use': 'browser-use'
}

# A repository with more merged pull requests than this links to the list instead.
MAX_LISTED_PRS = 2

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

def table_cell(text):
    # A bare `|` ends a markdown table cell, and `*` (as in `2**63`) can start emphasis.
    return text.replace('|', '\\|').replace('*', '\\*')

def format_stars(stars):
    if stars >= 1000:
        thousands = stars / 1000
        return f"{thousands:.0f}k" if thousands >= 100 else f"{thousands:.1f}k".replace('.0k', 'k')
    return str(stars)

def pr_link(pr):
    return f"[#{pr['number']}]({pr['url']})"

def repo_link(repo_name):
    disp_name = DISPLAY_NAMES.get(repo_name, repo_name.split('/')[1])
    return f"**[{disp_name}](https://github.com/{repo_name})**"

def build_section(nodes):
    repos = defaultdict(list)
    for pr in nodes:
        repo = pr.get('repository')
        if repo and not repo.get('isPrivate') and pr['state'] in ('OPEN', 'MERGED'):
            repos[repo['nameWithOwner']].append(pr)

    merged = {name: [p for p in prs if p['state'] == 'MERGED'] for name, prs in repos.items()}
    merged = {name: sorted(prs, key=lambda p: p['mergedAt'], reverse=True) for name, prs in merged.items() if prs}
    in_review = [p for prs in repos.values() for p in prs if p['state'] == 'OPEN']
    stars = {name: prs[0]['repository']['stargazerCount'] for name, prs in repos.items()}

    merged_count = sum(len(prs) for prs in merged.values())
    lines = [
        f"**{merged_count} merged pull requests in {len(merged)} projects**, plus {len(in_review)} in review — "
        "fixes and features in ML infrastructure, compilers, agent frameworks, and evaluation tooling.",
        "",
        "| Project | Stars | Merged | What I fixed |",
        "|:--------|------:|:-------|:-------------|",
    ]

    # Most merged pull requests first, then the larger project.
    for repo_name, prs in sorted(merged.items(), key=lambda item: (-len(item[1]), -stars[item[0]])):
        if len(prs) > MAX_LISTED_PRS:
            listed = f"[{len(prs)} PRs]({search_url(f'is:merged repo:{repo_name}')})"
        else:
            listed = ' · '.join(pr_link(p) for p in prs)
        impact = CURATED_IMPACTS.get(repo_name) or clean_pr_title(prs[0]['title'])
        lines.append(f"| {repo_link(repo_name)} | {format_stars(stars[repo_name])} | {listed} | {table_cell(impact)} |")

    if in_review:
        # Larger projects first; summarize the first few by name.
        in_review.sort(key=lambda p: (-p['repository']['stargazerCount'], -p['number']))
        names = []
        for p in in_review:
            name = DISPLAY_NAMES.get(p['repository']['nameWithOwner'], p['repository']['nameWithOwner'].split('/')[1])
            if name not in names:
                names.append(name)
        preview = ', '.join(names[:4]) + (', …' if len(names) > 4 else '')
        lines += [
            "",
            "<details>",
            f"<summary><b>In review ({len(in_review)})</b>: {preview}</summary>",
            "",
            "| Project | Stars | Pull request |",
            "|:--------|------:|:-------------|",
        ]
        for p in in_review:
            repo_name = p['repository']['nameWithOwner']
            lines.append(
                f"| {repo_link(repo_name)} | {format_stars(stars[repo_name])} | "
                f"{pr_link(p)} {table_cell(clean_pr_title(p['title']))} |"
            )
        lines += ["", "</details>"]

    lines += [
        "",
        f'<p align="center"><a href="{search_url("is:merged")}"><img src="https://img.shields.io/badge/GitHub-All_{merged_count}_merged_open_source_PRs-238636?style=for-the-badge&logo=github&logoColor=white" alt="All merged open source PRs" /></a></p>',
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
