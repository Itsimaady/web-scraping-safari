# 🌐 Web Scraping Safari

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python web scraper that extracts the top 5 trending repositories from GitHub's [Trending Page](https://github.com/trending) using `requests` and `BeautifulSoup`, and saves the data to a CSV file.

---

## 🚀 Features
✅ Scrapes repository names and links  
✅ Stores data in a CSV  
✅ Beginner-friendly and clean code  

---

## 📂 Project Files

| File | Purpose |
|-------|---------|
| `trending_scraper.py` | Python script to scrape trending repos |
| `trending_repos.csv` | CSV with scraped repository names & links |
| `README.md` | Project documentation |

---

## 💻 How to Run

```bash
# Clone the repo
git clone https://github.com/Itsimaady/web-scraping-safari.git
cd web-scraping-safari

# Install dependencies
pip install requests beautifulsoup4

# Run the scraper
python trending_scraper.py
