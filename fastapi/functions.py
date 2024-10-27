import pandas as pd
from bs4 import BeautifulSoup
import requests

endpoint = "http://ergast.com/api/f1/"

def update_driver_details():
    r = requests.get(endpoint + "2024/drivers.json")
    data = r.json()
    data = data['MRData']['DriverTable']['Drivers']
    df = pd.DataFrame(data)
    df.to_csv("./data/drivers.csv", index=True, header=True)

def update_race_schedule():
    r = requests.get(endpoint + "2024.json")
    data = r.json()
    data = data['MRData']['RaceTable']['Races']
    df = pd.DataFrame(data)
    df.to_csv("./data/schedule.csv", index=True, header=True)

def update_constructor_details():
    r = requests.get(endpoint + "2024/constructors.json")
    data = r.json()
    data = data['MRData']['ConstructorTable']['Constructors']
    df = pd.DataFrame(data)
    df.to_csv("./data/constructors.csv", index=True, header=True)


update_race_schedule()
update_driver_details()
update_constructor_details()