# graphs.py

import matplotlib.pyplot as plt

def plot_language_distribution(language_count, username):
    """
    Plot a pie chart of languages used in repos.
    """
    if not language_count:
        print("⚠️ No language data available to plot.")
        return

    labels = list(language_count.keys())
    sizes = list(language_count.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"Language Distribution for {username}")
    plt.axis("equal")  # Make pie circular
    plt.show()


def plot_stars_distribution(repos, username):
    """
    Plot a bar chart of stars per repo.
    """
    if not repos:
        print("⚠️ No repositories available to plot.")
        return

    repo_names = [repo["name"] for repo in repos]
    stars = [repo["stargazers_count"] for repo in repos]

    plt.figure(figsize=(10, 5))
    plt.bar(repo_names, stars, color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Stars")
    plt.title(f"Stars per Repository for {username}")
    plt.tight_layout()
    plt.show()
