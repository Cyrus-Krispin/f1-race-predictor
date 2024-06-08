import requests
from bs4 import BeautifulSoup
import pandas as pd

#url for all drivers
url = "https://www.formula1.com/en/drivers"

r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")

driver_urls = soup.find_all("a", class_="outline outline-offset-4 outline-brand-black group outline-0 focus-visible:outline-2")

driver_links = []
for driver in driver_urls:
    driver_links.append("https://www.formula1.com" + driver.get("href"))

driver_names = []
driver_numbers = []
driver_flags = []
driver_teams = []
driver_countries = []
driver_podiums = []
driver_points = []
driver_total_gps = []
driver_world_championships = []
driver_highest_race_finishes = []
driver_highest_grid_positions = []
driver_dates_of_birth = []
driver_places_of_birth = []

for driver_link in driver_links:
    url = driver_link
    r = requests.get(url).text
    soup = BeautifulSoup(r, "lxml")
    data = soup.find_all("div", class_="grid f1-grid grid-cols-1 tablet:grid-cols-2")[0]

    driver_names.append(data.h1.string)
    driver_numbers.append(data.find("p", class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne f1-utils-inline-image--loose text-greyDark").text)
    driver_flags.append(data.find("img", class_="f1-flag bg-brand-carbonBlack h-[32px] border border-greyLight rounded-xxs").get("src"))
    driver_teams.append(data.dl.find_all("dd")[0].string)
    driver_countries.append(data.dl.find_all("dd")[1].string)
    driver_podiums.append(data.dl.find_all("dd")[2].string)
    driver_points.append(data.dl.find_all("dd")[3].string)
    driver_total_gps.append(data.dl.find_all("dd")[4].string)
    driver_world_championships.append(data.dl.find_all("dd")[5].string)
    driver_highest_race_finishes.append(data.dl.find_all("dd")[6].string)
    driver_highest_grid_positions.append(data.dl.find_all("dd")[7].string)
    driver_dates_of_birth.append(data.dl.find_all("dd")[8].string)
    driver_places_of_birth.append(data.dl.find_all("dd")[9].string)

pd.DataFrame(data={"Name": driver_names, "No": driver_numbers, "Flag": driver_flags, "Team": driver_teams, "Country": driver_countries, "Podiums": driver_podiums, "Points": driver_points, "Total GPs": driver_total_gps, "World Championships": driver_world_championships, "Highest Race Finish": driver_highest_race_finishes, "Highest Grid Position": driver_highest_grid_positions, "Date of Birth": driver_dates_of_birth, "Place of Birth": driver_places_of_birth}).to_csv("driver_details.csv", index=False, header=True)