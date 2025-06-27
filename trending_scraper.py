import requests
from bs4 import BeautifulSoup
import csv

print("📡 Step 1: Sending request to GitHub Trending...")

URL = "https://github.com/trending"
response = requests.get(URL)

print(f"🌐 Step 2: Received status code: {response.status_code}")

if response.status_code != 200:
    print(f"❌ Error: Failed to load GitHub Trending page.")
    exit()

print("✅ Step 3: Parsing HTML content...")

soup = BeautifulSoup(response.text, 'html.parser')

# Inspecting structure
repo_list = soup.find_all('article', class_='Box-row')
print(f"📦 Step 4: Found {len(repo_list)} repositories.")

# If list is empty, notify
if not repo_list:
    print("⚠️ Warning: No repositories found. GitHub might have changed its layout.")
    exit()

# Extract top 5 only
repo_list = repo_list[:5]

data = []
for repo in repo_list:
    anchor = repo.h2.a
    repo_name = anchor.text.strip().replace('\n', '').replace(' ', '')
    repo_link = f"https://github.com{anchor['href']}"
    print(f"🔗 Found: {repo_name} → {repo_link}")
    data.append([repo_name, repo_link])

print("💾 Step 5: Saving to CSV...")

with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Repository Name', 'Link'])
    writer.writerows(data)

print("✅ Done: Data saved to 'trending_repos.csv'")
