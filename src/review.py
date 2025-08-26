def generate_review(username, repos, stats):
    """
    Generate a human-like review/summary about a GitHub user
    based on their repositories and stats.
    """

    total_repos = stats.get("total_repos", 0)
    total_stars = stats.get("total_stars", 0)
    average_stars = stats.get("average_stars", 0)
    top_repo = stats.get("top_repo", None)
    language_count = stats.get("language_count", {})

    # Identify most used language
    top_language = None
    if language_count:
        top_language = max(language_count, key=language_count.get)

    review_lines = []

    # Start of review
    if total_repos == 0:
        return f"📝 User **{username}** exists but hasn’t created any repositories yet."

    review_lines.append(f"📝 **GitHub Review for {username}:**")

    # Repository activity
    review_lines.append(f"- This developer has **{total_repos} repositories** in total.")

    if top_language:
        review_lines.append(f"- Their most used language is **{top_language}** "
                            f"({language_count[top_language]} repo(s)).")

    # Stars analysis
    if total_stars > 0:
        review_lines.append(f"- Collectively, their repositories have earned **{total_stars} stars**, "
                            f"with an average of about **{average_stars:.1f} stars per repo**.")
    else:
        review_lines.append("- Currently, their repositories have not received any stars yet.")

    # Highlight top repo
    if top_repo:
        review_lines.append(f"- Their most popular repository is **{top_repo['name']}** "
                            f"with **{top_repo['stargazers_count']} stars** "
                            f"(👉 {top_repo['html_url']}).")

    # Closing statement
    if total_stars > 50:
        review_lines.append("✨ Overall, this profile shows strong community recognition "
                            "and active contributions.")
    elif total_repos > 5:
        review_lines.append("📂 This profile reflects a developer exploring and building steadily.")
    else:
        review_lines.append("🌱 This profile seems to be in its early stages, "
                            "with room for growth and contributions.")

    return "\n".join(review_lines)
