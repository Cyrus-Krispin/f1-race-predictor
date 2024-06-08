import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/drivers/max-verstappen"

r = requests.get(url).text
soup = BeautifulSoup(r, "lxml")
data = soup.find_all("div", class_="grid f1-grid grid-cols-1 tablet:grid-cols-2")[0]

driver_name = data.h1.string