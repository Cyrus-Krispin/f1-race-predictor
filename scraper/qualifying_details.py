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
positions = []
driver_numbers = []
driver_names = []
driver_teams = []
q1_times = []
q2_times = []
q3_times = []
laps = []

for race in races:
    url = race.get("href")
    r = requests.get("https://www.formula1.com" + url[:-16] + "qualifying.html").text
    
    soup = BeautifulSoup(r, "lxml")

    data = soup.find("table", class_="resultsarchive-table").find("tbody").find_all("tr")

    for row in data:
        race_names.append(race.text.strip())
        val = row.find_all("td")
        positions.append(val[1].string)
        driver_numbers.append(val[2].string)
        names = val[3].find_all("span")
        driver_names.append(names[0].string + " " + names[1].string)
        driver_teams.append(val[4].string)
        q1_times.append(val[5].string)
        q2_times.append(val[6].string)
        q3_times.append(val[7].string)
        laps.append(val[8].string)


pd.DataFrame(data={"Race": race_names, "Qualifying Pos": positions, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Q1": q1_times, "Q2": q2_times, "Q3": q3_times, "Qualifying Laps": laps}).to_csv("qualifying_details.csv", index=False, header=True)
