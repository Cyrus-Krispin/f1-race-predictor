import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all teams
url = "https://www.formula1.com/en/teams"
r = requests.get(url).text

soup = BeautifulSoup(r, "lxml")

# Extracting the list of teams
teams = soup.find("div", class_="flex flex-col tablet:grid tablet:grid-cols-12 [&>*]:col-span-12 tablet:[&>*]:col-span-6 gap-xl laptop:[&>*]:col-span-6 desktop:[&>*]:col-span-6").findChildren("a")

team_links = []
for team in teams:
    team_links.append("https://www.formula1.com" + team.get("href"))

team_names = []
team_full_names = []
team_bases = []
team_chiefs = []
team_technical_chiefs = []
team_chassis = []
team_power_units = []
team_first_seasons = []
team_world_championships = []
team_highest_race_finishes = []
team_pole_positions = []
team_fastest_laps = []

for team_link in team_links:
    url = team_link
    r = requests.get(url).text
    soup = BeautifulSoup(r, "lxml")
    
    data = soup.find("dl").find_all("dd")

    team_names.append(soup.find("h1", class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne").string)
    team_full_names.append(data[0].string)
    team_bases.append(data[1].string)
    team_chiefs.append(data[2].string)
    team_technical_chiefs.append(data[3].string)
    team_chassis.append(data[4].string)
    team_power_units.append(data[5].string)
    team_first_seasons.append(data[6].string)
    team_world_championships.append(data[7].string)
    team_highest_race_finishes.append(data[8].string)
    team_pole_positions.append(data[9].string)
    team_fastest_laps.append(data[10].string)

pd.DataFrame(data={"Name": team_names, "Full Name": team_full_names, "Base": team_bases, "Chief": team_chiefs, "Technical Chief": team_technical_chiefs, "Chassis": team_chassis, "Power Unit": team_power_units, "First Season": team_first_seasons, "World Championships": team_world_championships, "Highest Race Finish": team_highest_race_finishes, "Pole Positions": team_pole_positions, "Fastest Laps": team_fastest_laps}).to_csv("team_details.csv", index=False, header=True)

