import requests
from bs4 import BeautifulSoup

# URL to scrape
r = requests.get("https://www.formula1.com/en/drivers").text
soup = BeautifulSoup(r, "lxml")


# Extracting the first and last names of the drivers
first = soup.find_all("p", class_="f1-heading tracking-normal text-fs-12px leading-tight uppercase font-normal non-italic f1-heading__body font-formulaOne")
last = soup.find_all("p", class_="f1-heading tracking-normal text-fs-18px leading-tight uppercase font-bold non-italic f1-heading__body font-formulaOne")

f = BeautifulSoup(str(first), "lxml")
l = BeautifulSoup(str(last), "lxml")


print(f.get_text())
print(l.get_text())