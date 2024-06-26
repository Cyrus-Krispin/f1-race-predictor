import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all races

url = "https://www.formula1.com/en/results.html/2024/races.html"
r = requests.get(url).text

soup = BeautifulSoup(r, "lxml")

# Extracting

race_names = []
stops = []
driver_numbers = []
driver_names = []
driver_teams = []
lap = []
time_of_days = []
pit_stop_times = []
total_pit_stop_times = []

races = soup.find_all("a", class_="dark bold ArchiveLink")

for race in races:
        url = race.get("href")
        r = requests.get("https://www.formula1.com" + url[:-16] + "pit-stop-summary.html").text
        soup = BeautifulSoup(r, "lxml")

        data = soup.find("table", class_="resultsarchive-table").find("tbody").find_all("tr")

        for row in data:
            race_names.append(race.text.strip())
            val = row.find_all("td")
            stops.append(val[1].string)
            driver_numbers.append(val[2].string)
            names = val[3].find_all("span")
            driver_names.append(names[0].string + " " + names[1].string)
            driver_teams.append(val[4].string)
            lap.append(val[5].string)
            time_of_days.append(val[6].string)
            pit_stop_times.append(val[7].string)
            total_pit_stop_times.append(val[8].string)
        
pd.DataFrame(data={"Race": race_names, "Stops": stops, "No": driver_numbers, "Name": driver_names, "Team": driver_teams, "Pit Stop Lap": lap, "Time of Day": time_of_days, "Pit Stop Time": pit_stop_times, "Total Pit Stop Time": total_pit_stop_times}).to_csv("pit_stop_summary.csv", index=False, header=True)