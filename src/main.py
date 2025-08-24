# import requests

# # 1. Get GitHub username
# username = input("Enter GitHub username: ")

# # 2. Fetch repo list
# url = f"https://api.github.com/users/{username}/repos"
# response = requests.get(url)

# if response.status_code == 200:
#     repos = response.json()

#     if repos:  # check if user actually has repos
#         # Sort repos by stars
#         repos.sort(key=lambda r: r["stargazers_count"], reverse=True)

#         print(f"Total repositories: {len(repos)}")
#         print("Repo names:")
#         for repo in repos:
#             name = repo["name"]
#             stars = repo["stargazers_count"]  # No.of Stars
#             forks = repo["forks_count"]      # No.of Forks
#             print(f"- {name} | Stars: {stars} | Forks: {forks}")

#         # Most starred repo
#         most_starred = repos[0]
#         print("\n🔥 Most starred repo:")
#         print(f"{most_starred['name']} | Stars: {most_starred['stargazers_count']} | Forks: {most_starred['forks_count']}")

#         # Most forked repo (need separate sort)
#         repos_sorted_by_forks = sorted(repos, key=lambda r: r["forks_count"], reverse=True)
#         most_forked = repos_sorted_by_forks[0]
#         print("\n🍴 Most forked repo:")
#         print(f"{most_forked['name']} | Stars: {most_forked['stargazers_count']} | Forks: {most_forked['forks_count']}")

#     else:
#         print("This user has no repositories.")

# else:
#     print("Failed to fetch data. Check the username or your connection.")

import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()

    if not repos:
        print("ℹ️ This user exists but has no repositories.")
    else:
        repos.sort(key=lambda r: r["stargazers_count"], reverse=True)

        print(f"\n📂 Total repositories: {len(repos)}\n")
        print("🔎 Repository Details:")

        language_count = {}

        for repo in repos:
            name = repo["name"]
            stars = repo["stargazers_count"]
            forks = repo["forks_count"]
            repo_url = repo["html_url"]
            language = repo["language"] or "Unknown"

            language_count[language] = language_count.get(language, 0) + 1

            print(f"- {name} | ⭐ {stars} | 🍴 {forks} | {language} | {repo_url}")

        top_repo = repos[0]
        print(f"\n🏆 Most Starred Repo: {top_repo['name']} ({top_repo['stargazers_count']} ⭐)")
        print(f"   👉 {top_repo['html_url']}")

        print("\n📊 Language Breakdown:")
        for lang, count in language_count.items():
            print(f"- {lang}: {count} repo(s)")

        print("\n✅ Analysis complete. 🚀")

elif response.status_code == 404:
    print("❌ No such GitHub user exists. Please check the username.")

else:
    print(f"⚠️ Failed to fetch data. HTTP Status: {response.status_code}")
