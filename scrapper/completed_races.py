import requests
from bs4 import BeautifulSoup
import csv

r = requests.get("https://www.formula1.com/en/results.html/2024/races.html").text
soup = BeautifulSoup(r, "lxml")

# Extracting the list of races

races = soup.find_all("a", class_="dark bold ArchiveLink")

races_list = BeautifulSoup(str(races), "lxml")

for race in races_list.stripped_strings:
    print(race)

# Writing

with open("file.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(races_list.stripped_strings)