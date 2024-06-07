import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.formula1.com/en/results.html/2024/races.html")

soup = BeautifulSoup(r.text, "lxml")

# Extracting the names
race_items = soup.find_all('a', {'data-name': 'meetingKey', 'data-value': lambda x: x and x != ""})

race_names = [item.span.text for item in race_items]
print(race_names)

# writing the names to a file

pd.DataFrame(race_names).to_csv("output.csv", index=False, header=False)