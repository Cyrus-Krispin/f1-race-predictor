import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all races
url = "https://www.formula1.com/en/results.html/2024/races/1229/bahrain/race-result.html"

r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")

# Extracting
data = soup.find("tbody")
rows = data.find_all("tr")

pos = []
driver_numbers = []
driver_names = []
driver_teams = []
laps = []
total_time = []
points = []

for row in rows:
    val = row.find_all("td")
    pos.append(val[1].string)
    driver_numbers.append(val[2].string)
    names = list(val[3].children)
    driver_names.append(names[0].string + " " + names[1].string)
    driver_teams.append(val[4].string)
    laps.append(val[5].string)
    total_time.append(val[6].string)
    points.append(val[7].string)

pd.DataFrame(data={"Pos": pos, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Laps": laps, "Time": total_time, "Points": points}).to_csv("race_details.csv", index=False, header=True)

