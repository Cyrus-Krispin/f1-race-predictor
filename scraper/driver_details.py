import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/drivers/max-verstappen"

r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")

data = soup.find_all("div", class_="grid f1-grid grid-cols-1 tablet:grid-cols-2")[0]

driver_name = data.h1.string
driver_number_data = data.find("p", class_="f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne f1-utils-inline-image--loose text-greyDark").text
driver_flag = data.find("img", class_="f1-flag bg-brand-carbonBlack h-[32px] border border-greyLight rounded-xxs").get("src")
driver_team = data.dl.find_all("dd")[0].string
driver_country = data.dl.find_all("dd")[1].string
driver_podiums = data.dl.find_all("dd")[2].string
driver_points = data.dl.find_all("dd")[3].string
driver_total_gp = data.dl.find_all("dd")[4].string
driver_world_championships = data.dl.find_all("dd")[5].string
driver_highest_race_finish = data.dl.find_all("dd")[6].string
driver_highest_grid_position = data.dl.find_all("dd")[7].string
driver_date_of_birth = data.dl.find_all("dd")[8].string
driver_place_of_birth = data.dl.find_all("dd")[9].string

print(driver_name, driver_number_data, driver_flag, driver_team, driver_country, driver_podiums, driver_points, driver_total_gp, driver_world_championships, driver_highest_race_finish, driver_highest_grid_position, driver_date_of_birth, driver_place_of_birth)
