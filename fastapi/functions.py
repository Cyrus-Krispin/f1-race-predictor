import pandas as pd
import numpy as np
import requests

endpoint = "http://ergast.com/api/f1/"

def update_driver_details():
    r = requests.get(endpoint + "2024/drivers.json")
    data = r.json()
    data = data['MRData']['DriverTable']['Drivers']
    df = pd.DataFrame(data)
    df.drop(columns=['url'], inplace=True)
    df.to_csv("../data/drivers.csv", index=True, header=True)

def update_race_schedule():
    r = requests.get(endpoint + "2024.json")
    data = r.json()
    data = data['MRData']['RaceTable']['Races']
    df = pd.DataFrame(data)
    df.drop(columns=['url', 'Circuit', 'date', 'time'], inplace=True)
    df.to_csv("../data/schedule.csv", index=True, header=True)

def update_constructor_details():
    r = requests.get(endpoint + "2024/constructors.json")
    data = r.json()
    data = data['MRData']['ConstructorTable']['Constructors']
    df = pd.DataFrame(data)
    df.drop(columns=['url'], inplace=True)
    df.to_csv("../data/constructors.csv", index=True, header=True)

def getcurrent():
    r = requests.get(endpoint + "current/last.json")
    data = r.json()
    data = data['MRData']['RaceTable']
    return data['round']

def update_race_results():
    df = pd.DataFrame(columns=['raceId', 'driverId', 'constructorId', 'grid', 'position', 'points', 'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapTime', 'fastestLapSpeed'])
    current_round = getcurrent()
    for i in range(1, int(current_round) + 1):
        r = requests.get(endpoint + "2024/" + str(i) + "/results.json")
        data = r.json()
        data = data['MRData']['RaceTable']['Races'][0]['Results']
        for j in range(len(data)):
            driverId = data[j]['Driver']['driverId']
            constructorId = data[j]['Constructor']['constructorId']
            grid = data[j]['grid']
            position = data[j]['position']
            points = data[j]['points']
            laps = data[j]['laps']

            if 'Time' not in data[j]:
                time = np.nan
                milliseconds = np.nan
            else:
                time = data[j]['Time']['time']
                milliseconds = data[j]['Time']['millis']

            if 'FastestLap' not in data[j]:
                rank = np.nan
                fastestLap = np.nan
                fastestLapTime = np.nan
                fastestLapSpeed = np.nan
            else:
                rank = data[j]['FastestLap']['rank']
                fastestLap = data[j]['FastestLap']['lap']
                fastestLapTime = data[j]['FastestLap']['Time']['time']
                fastestLapSpeed = data[j]['FastestLap']['AverageSpeed']['speed']

            df = df._append({'raceId': i, 'driverId': driverId, 'constructorId': constructorId, 'grid': grid, 'position': position, 'points': points, 'laps': laps, 'time': time, 'milliseconds': milliseconds, 'fastestLap': fastestLap, 'rank': rank, 'fastestLapTime': fastestLapTime, 'fastestLapSpeed': fastestLapSpeed}, ignore_index=True)

    df.to_csv("../data/results.csv", index=True, header=True)
            

def update_all():
    update_race_schedule()
    update_driver_details()
    update_constructor_details()

update_race_results()