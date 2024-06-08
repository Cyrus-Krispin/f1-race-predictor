import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/results.html/2024/team.html"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

team_items = soup.find_all("a", class_="dark bold uppercase ArchiveLink")

for item in team_items:
    print(item.get_text())