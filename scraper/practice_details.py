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
        for row in data:
            race_names.append(race.text.strip())
            val = row.find_all("td")
            pos.append(val[1].string)
            driver_numbers.append(val[2].string)
            names = val[3].find_all("span")
            driver_names.append(names[0].string + " " + names[1].string)
            driver_teams.append(val[4].string)
            fastest_laps.append(val[5].string)
            gaps.append(val[6].text.strip())
            laps.append(val[7].string)

    pd.DataFrame(data={"Race": race_names, "Pos": pos, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Fastest Lap": fastest_laps, "Gap": gaps, "Laps": laps}).to_csv(practice + "_details.csv", index=False, header=True)