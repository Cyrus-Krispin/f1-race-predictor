import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all races

url = "https://www.formula1.com/en/results.html/2024/races.html"
r = requests.get(url).text

soup = BeautifulSoup(r, "lxml")

# Extracting

race_names = []
pos = []
driver_numbers = []
driver_names = []
driver_teams = []
qualifying_times = []


races = soup.find_all("a", class_="dark bold ArchiveLink")

for race in races:
    url = race.get("href")
    r = requests.get("https://www.formula1.com" + url[:-16] + "starting-grid.html").text
    
    soup = BeautifulSoup(r, "lxml")

    data = soup.find("table", class_="resultsarchive-table").find("tbody").find_all("tr")

    for row in data:
        race_names.append(race.text.strip())
        val = row.find_all("td")
        pos.append(val[1].string)
        driver_numbers.append(val[2].string)
        names = val[3].find_all("span")
        driver_names.append(names[0].string + " " + names[1].string)
        driver_teams.append(val[4].string)
        qualifying_times.append(val[5].string)

pd.DataFrame(data={"Race": race_names, "Starting Pos": pos, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Qualifying Time": qualifying_times}).to_csv("starting_positions.csv", index=False, header=True)