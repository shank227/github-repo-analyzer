# calculations.py

def get_repo_stats(repos):
    """
    Calculate total repos, total stars, average stars, most starred repo,
    and language breakdown.
    """
    total_repos = len(repos)
    total_stars = sum(repo["stargazers_count"] for repo in repos)
    average_stars = total_stars / total_repos if total_repos > 0 else 0

    # Most starred repo
    top_repo = max(repos, key=lambda r: r["stargazers_count"], default=None)

    # Language breakdown
    language_count = {}
    for repo in repos:
        language = repo["language"] or "Unknown"
        language_count[language] = language_count.get(language, 0) + 1

    return {
        "total_repos": total_repos,
        "total_stars": total_stars,
        "average_stars": average_stars,   # ✅ ensure this is here
        "top_repo": top_repo,
        "language_count": language_count,
    }
