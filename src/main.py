import requests
from calculations import get_repo_stats
from graphs import plot_language_distribution, plot_stars_distribution
from review import generate_review

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()

    if not repos:
        print("ℹ️ This user exists but has no repositories.")
    else:
        repos.sort(key=lambda r: r["stargazers_count"], reverse=True)

        stats = get_repo_stats(repos)

        print(f"\n📂 Total repositories: {stats['total_repos']}")
        print(f"⭐ Total stars: {stats['total_stars']}")
        print(f"📈 Average stars per repo: {stats['average_stars']}\n")

        print("🔎 Repository Details:")
        for repo in repos:
            print(f"- {repo['name']} | ⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']} | {repo['language'] or 'Unknown'} | {repo['html_url']}")

        if stats['top_repo']:
            print(f"\n🏆 Most Starred Repo: {stats['top_repo']['name']} ({stats['top_repo']['stargazers_count']} ⭐)")
            print(f"   👉 {stats['top_repo']['html_url']}")

        print("\n📊 Language Breakdown:")
        for lang, count in stats['language_count'].items():
            print(f"- {lang}: {count} repo(s)")
        
        # after fetching stats
        plot_language_distribution(stats["language_count"], username)
        plot_stars_distribution(repos, username)

        stats = get_repo_stats(repos)
        print("\n" + generate_review(username, repos, stats))

        print("\n✅ Analysis complete. 🚀")

elif response.status_code == 404:
    print("❌ No such GitHub user exists. Please check the username.")

else:
    print(f"⚠️ Failed to fetch data. HTTP Status: {response.status_code}")
