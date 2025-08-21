import requests

# 1. Get GitHub username
username = input("Enter GitHub username: ")

# 2. Fetch repo list
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    print(f"Total repositories: {len(repos)}")
    print("Repo names:")
    for repo in repos:
        print("-", repo["name"])
else:
    print("Failed to fetch data. Check the username or your connection.")
