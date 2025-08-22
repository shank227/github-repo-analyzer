import requests

# 1. Get GitHub username
username = input("Enter GitHub username: ")

# 2. Fetch repo list
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    repos.sort(key=lambda r: r["stargazers_count"], reverse=True)
    print(f"Total repositories: {len(repos)}")
    print("Repo names:")
    for repo in repos:
        name = repo["name"]
        stars = repo["stargazers_count"] # No.of Stars
        forks = repo["forks_count"] # No.of Forks
        print(f"- {name} | Stars: {stars} | Forks: {forks}")

else:
    print("Failed to fetch data. Check the username or your connection.")
