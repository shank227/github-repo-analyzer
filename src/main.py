import requests

# 1. Get GitHub username
username = input("Enter GitHub username: ")

# 2. Fetch repo list
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()

    if repos:  # check if user actually has repos
        # Sort repos by stars
        repos.sort(key=lambda r: r["stargazers_count"], reverse=True)

        print(f"Total repositories: {len(repos)}")
        print("Repo names:")
        for repo in repos:
            name = repo["name"]
            stars = repo["stargazers_count"]  # No.of Stars
            forks = repo["forks_count"]      # No.of Forks
            print(f"- {name} | Stars: {stars} | Forks: {forks}")

        # Most starred repo
        most_starred = repos[0]
        print("\n🔥 Most starred repo:")
        print(f"{most_starred['name']} | Stars: {most_starred['stargazers_count']} | Forks: {most_starred['forks_count']}")

        # Most forked repo (need separate sort)
        repos_sorted_by_forks = sorted(repos, key=lambda r: r["forks_count"], reverse=True)
        most_forked = repos_sorted_by_forks[0]
        print("\n🍴 Most forked repo:")
        print(f"{most_forked['name']} | Stars: {most_forked['stargazers_count']} | Forks: {most_forked['forks_count']}")

    else:
        print("This user has no repositories.")

else:
    print("Failed to fetch data. Check the username or your connection.")

#hello universe
