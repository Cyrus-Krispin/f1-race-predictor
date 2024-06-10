import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all races
url = "https://www.formula1.com/en/results.html/2024/races.html"

r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")

races = soup.find_all("a", class_="dark bold ArchiveLink")

race_names = []
pos = []
driver_numbers = []
driver_names = []
driver_teams = []
laps = []
total_time = []
points = []


for race in races:
    url = race.get("href")
    r = requests.get("https://www.formula1.com" + url).text
    soup = BeautifulSoup(r, "lxml")
    data = soup.find("tbody")
    rows = data.find_all("tr")


    for row in rows:
        race_names.append(race.text.strip())
        val = row.find_all("td")
        pos.append(val[1].string)
        driver_numbers.append(val[2].string)
        names = val[3].find_all("span")
        driver_names.append(names[0].string + " " + names[1].string)
        driver_teams.append(val[4].string)
        laps.append(val[5].string)
        total_time.append(val[6].text)
        points.append(val[7].string)

pd.DataFrame(data={"Race": race_names, "Pos": pos, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Laps": laps, "Time": total_time, "Points": points}).to_csv("race_details.csv", index=False, header=True)

