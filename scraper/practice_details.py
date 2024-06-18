import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all races

url = "https://www.formula1.com/en/results.html/2024/races.html"
r = requests.get(url).text

soup = BeautifulSoup(r, "lxml")

# Extracting

races = soup.find_all("a", class_="dark bold ArchiveLink")

race_names = []
pos = []
driver_numbers = []
driver_names = []
driver_teams = []
fastest_laps = []
gaps = []
laps = []

practices = ["practice-1", "practice-2", "practice-3"]

for practice in practices:
    for race in races:
        url = race.get("href")
        r = requests.get("https://www.formula1.com" + url[:-16] + practice + ".html").text
        soup = BeautifulSoup(r, "lxml")

        data = soup.find("table", class_="resultsarchive-table").find("tbody").find_all("tr")
