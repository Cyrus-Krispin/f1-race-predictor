import pandas as pd
from bs4 import BeautifulSoup
import requests

endpoint = "http://ergast.com/api/f1/"

def update_race_details():
    r = requests.get(endpoint + "2024.json")
    #TODO: process json data
    data = r.json()
    df = pd.DataFrame(data)
    df.to_csv("./data/sessions.csv", index=False, header=True)

def update_driver_details():
    r = requests.get(endpoint + "drivers?session_key=7763")
    data = r.json()
    df = pd.DataFrame(data)
    df.to_csv("./data/drivers.csv", index=False, header=True)

update_race_details()