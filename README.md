# GitHub Repo Analyzer

A Python-based project that analyzes GitHub users’ repositories and provides **detailed insights, statistics, and visualizations**.

---

## 🔍 What It Does
- Fetches **all public repositories** of a given GitHub user
- Displays details: **name, stars, forks, language, and repo link**
- Performs **calculations**:
  - Total repositories 📂
  - Total stars ⭐
  - Average stars per repo 📊
  - Most starred repository 🏆
- Generates **graphs**:
  - Stars distribution (bar chart)
  - Forks distribution (bar chart)
  - Language usage (pie chart)
- Provides a **written review** summarizing user activity

---

## 📂 Project Structure
The project is organized into modular Python files for clarity and maintainability:
project1/
└── github_repo_analyzer/
└── src/
  ├── main.py # Entry point
  ├── calculations.py # Repo statistics & metrics
  ├── graphs.py # Data visualizations
└── review.py # Automated written analysis

## 📂 Sample Output
📂 Total repositories: 15

🔎 Repository Details:
- sample-repo | ⭐ 42 | 🍴 7 | Python | https://github.com/user/sample-repo

🏆 Most Starred Repo: sample-repo (42 ⭐)
   👉 https://github.com/user/sample-repo

📊 Language Breakdown:
- Python: 10 repo(s)
- JavaScript: 3 repo(s)
- C++: 2 repo(s)

✅ User Analysis:
This developer has a strong focus on Python, with an active set of projects.
While most repositories have moderate traction, the standout project
`sample-repo` demonstrates significant visibility.

## 🚀 Features
- Built with requests for fetching GitHub data
- Uses matplotlib for generating graphs
- Custom modular design for scalability (easy to extend with more analysis features)
- Lightweight and beginner-friendly

## 📌 Future Enhancements
- Export results to PDF/HTML reports
- Web-based interactive dashboard (like GitHub profile visualizer)
- More advanced metrics (commit activity, contribution trends)


---

## 📢 Note
This is **v1.0** — feel free to contribute or drop suggestions.  
Open to improvements, ideas, and collaboration.  

**Hasta luego!** 🌟  
*(137-day Duolingo Spanish streak 💪)*

