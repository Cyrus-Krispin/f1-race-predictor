import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.formula1.com/en/drivers")
print(r.text)