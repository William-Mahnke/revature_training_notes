import httpx

def get_repo_summary(owner: str, name: str) -> dict | None:
    """Fetch a public GitHub repo and return a trimmed summary, or None on failure."""
    with httpx.Client(
        base_url="https://api.github.com",
        headers={"Accept": "application/vnd.github+json"},
        timeout=10.0,
    ) as client:
        try:
            resp = client.get(f"/repos/{owner}/{name}")
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            print(f"GitHub returned {exc.response.status_code} for {owner}/{name}")
            return None
        except httpx.RequestError as exc:
            print(f"Network error reaching GitHub: {exc}")
            return None

        data = resp.json()
        return {
            "full_name": data["full_name"],
            "stars": data["stargazers_count"],
            "language": data["language"],
            "open_issues": data["open_issues_count"],
        }


if __name__ == "__main__":
    summary = get_repo_summary("encode", "httpx")
    if summary:
        print(summary)
    # -> {'full_name': 'encode/httpx', 'stars': ..., 'language': 'Python', ...}