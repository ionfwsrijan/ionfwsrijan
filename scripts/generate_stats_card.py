#!/usr/bin/env python3
"""Generate a self-hosted GitHub stats card (SVG) using the GitHub GraphQL API.

Env vars:
  GITHUB_TOKEN     required  token used for the API (Actions provides one)
  GH_LOGIN         optional  GitHub username        (default: ionfwsrijan)
  CARD_TITLE       optional  title shown on the card (default: "Srijan's Stats")
  OUT_PATH         optional  where to write the SVG  (default: assets/stats-card.svg)
  INCLUDE_PRIVATE  optional  "true" adds private contribution counts to Commits
                             (only works with a personal access token)
"""
import datetime
import json
import os
import sys
import urllib.request
from xml.sax.saxutils import escape

LOGIN = os.environ.get("GH_LOGIN", "ionfwsrijan")
TITLE = os.environ.get("CARD_TITLE", "Srijan's Stats")
OUT = os.environ.get("OUT_PATH", "assets/stats-card.svg")
INCLUDE_PRIVATE = os.environ.get("INCLUDE_PRIVATE", "true").lower() == "true"


def gql(query, variables=None):
    token = os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-card",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]


def fetch_stats(login):
    base = gql(
        """
        query($login: String!) {
          user(login: $login) {
            createdAt
            followers { totalCount }
            pullRequests { totalCount }
            issues { totalCount }
            repositories(ownerAffiliations: OWNER) { totalCount }
          }
        }
        """,
        {"login": login},
    )["user"]

    # Total stars across owned repos (paginated)
    stars, cursor = 0, None
    while True:
        page = gql(
            """
            query($login: String!, $cursor: String) {
              user(login: $login) {
                repositories(ownerAffiliations: OWNER, first: 100, after: $cursor) {
                  nodes { stargazerCount }
                  pageInfo { hasNextPage endCursor }
                }
              }
            }
            """,
            {"login": login, "cursor": cursor},
        )["user"]["repositories"]
        stars += sum(n["stargazerCount"] for n in page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]

    # Commits + reviews: contributionsCollection only spans 1 year, so sum per year
    start_year = int(base["createdAt"][:4])
    end_year = datetime.datetime.now(datetime.timezone.utc).year
    blocks = []
    for y in range(start_year, end_year + 1):
        blocks.append(
            f'y{y}: contributionsCollection(from: "{y}-01-01T00:00:00Z", '
            f'to: "{y}-12-31T23:59:59Z") '
            "{ totalCommitContributions restrictedContributionsCount "
            "totalPullRequestReviewContributions }"
        )
    years = gql(
        "query($login: String!) { user(login: $login) { " + " ".join(blocks) + " } }",
        {"login": login},
    )["user"]

    commits = reviews = 0
    for v in years.values():
        commits += v["totalCommitContributions"]
        if INCLUDE_PRIVATE:
            commits += v["restrictedContributionsCount"]
        reviews += v["totalPullRequestReviewContributions"]

    return {
        "stars": stars,
        "commits": commits,
        "prs": base["pullRequests"]["totalCount"],
        "issues": base["issues"]["totalCount"],
        "repos": base["repositories"]["totalCount"],
        "reviews": reviews,
        "followers": base["followers"]["totalCount"],
    }


def calculate_rank(s):
    """Percentile-based rank (same idea as github-readme-stats)."""
    exp_cdf = lambda x: 1 - 2 ** -x
    log_cdf = lambda x: x / (1 + x)
    weights = {"commits": 2, "prs": 3, "issues": 1, "reviews": 1, "stars": 4, "followers": 1}
    score = (
        weights["commits"] * exp_cdf(s["commits"] / 250)
        + weights["prs"] * exp_cdf(s["prs"] / 50)
        + weights["issues"] * exp_cdf(s["issues"] / 25)
        + weights["reviews"] * exp_cdf(s["reviews"] / 2)
        + weights["stars"] * log_cdf(s["stars"] / 50)
        + weights["followers"] * log_cdf(s["followers"] / 10)
    )
    percentile = (1 - score / sum(weights.values())) * 100
    thresholds = [1, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100]
    levels = ["S+", "S", "A+", "A", "A-", "B+", "B", "B-", "C"]
    for t, lvl in zip(thresholds, levels):
        if percentile <= t:
            return lvl
    return "C"


def fmt(n):
    if n >= 1000:
        return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n)


def render_svg(title, stats, rank):
    font = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    items = [
        ("Stars", fmt(stats["stars"])),
        ("Commits", fmt(stats["commits"])),
        ("PRs", fmt(stats["prs"])),
        ("Issues", fmt(stats["issues"])),
        ("Repos", fmt(stats["repos"])),
    ]
    boxes = []
    for i, (label, value) in enumerate(items):
        x = 36 + i * 135.5
        cx = x + 60.5
        boxes.append(
            f'<rect x="{x}" y="117" width="121" height="104" rx="12" '
            f'fill="#161c18" stroke="#1f2922" stroke-width="1"/>'
            f'<text x="{cx}" y="153" text-anchor="middle" font-family="{font}" '
            f'font-size="14" font-weight="600" fill="#8a8a8a">{escape(label)}</text>'
            f'<text x="{cx}" y="193" text-anchor="middle" font-family="{font}" '
            f'font-size="26" font-weight="700" fill="#ffffff">{escape(value)}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="730" height="250" viewBox="0 0 730 250" role="img" aria-label="{escape(title)}">
  <rect width="730" height="250" rx="16" fill="#141414"/>
  <text x="36" y="76" font-family="{font}" font-size="24" font-weight="700" fill="#ffffff">{escape(title)}</text>
  <rect x="574.5" y="44.5" width="123" height="46" rx="23" fill="#1a2a1f" stroke="#2c4a35" stroke-width="1"/>
  <text x="595" y="73" font-family="{font}" font-size="12" font-weight="700" letter-spacing="2" fill="#8a8a8a">RANK</text>
  <text x="646" y="74" font-family="{font}" font-size="22" font-weight="800" fill="#ffffff">{escape(rank)}</text>
  {''.join(boxes)}
</svg>
"""


def main():
    stats = fetch_stats(LOGIN)
    rank = calculate_rank(stats)
    svg = render_svg(TITLE, stats, rank)
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {OUT}: {stats} rank={rank}")


if __name__ == "__main__":
    main()
