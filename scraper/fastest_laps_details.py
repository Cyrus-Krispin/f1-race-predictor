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
laps = []
time_of_days = []
fastest_times = []
average_speeds = []

for race in races:
    url = race.get("href")
    r = requests.get("https://www.formula1.com" + url[:-16] + "fastest-laps.html").text
    
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
        laps.append(val[5].string)
        time_of_days.append(val[6].string)
        fastest_times.append(val[7].string)
        average_speeds.append(val[8].string)

pd.DataFrame(data={"Race": race_names, "Fastest Order": pos, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Laps": laps, "Time of Day": time_of_days, "Fastest Time": fastest_times, "Average Speed": average_speeds}).to_csv("fastest_laps_details.csv", index=False, header=True)