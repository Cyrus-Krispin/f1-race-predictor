import pandas as pd
import requests

endpoint = "https://api.openf1.org/v1/"

def get_meetings():
    print("Fetching meetings data")
    response = requests.get(endpoint + "meetings")
    if response.status_code == 200:
        print("Meetings data fetched successfully")
        return response.json()
    else:
        print(f"Failed to fetch meetings data: {response.status_code}")
        response.raise_for_status()

def update_all_data():
    print("Starting data update process")
    df = pd.DataFrame(columns=["meeting_key", "race_name", "driver_number", "driver_name", "practice_1", "practice_2", "practice_3", "sprint_quali", "sprint_race", "qualifying", "race"])
    meetings = get_meetings()
    for meeting in meetings:
        meeting_key = meeting["meeting_key"]
        race_name = meeting["meeting_official_name"]
        if meeting['meeting_name'] == "Pre-Season Testing":
            print(f"Skipping Pre-Season Testing meeting: {meeting_key} ({race_name})")
            continue
        print(f"Fetching sessions for meeting: {meeting_key} ({race_name})")
        sessions_response = requests.get(endpoint + f"sessions?meeting_key={meeting_key}")
        if sessions_response.status_code == 200:
            sessions = sessions_response.json()
        else:
            print(f"Failed to fetch sessions for meeting {meeting_key} ({race_name}): {sessions_response.status_code}")
            sessions_response.raise_for_status()
        
        drivers = set()
        for session in sessions:
            session_key = session["session_key"]
            print(f"Fetching drivers for session: {session_key} ({race_name})")
            drivers_response = requests.get(endpoint + f"drivers?session_key={session_key}")
            if drivers_response.status_code == 200:
                session_drivers = drivers_response.json()
            else:
                print(f"Failed to fetch drivers for session {session_key} ({race_name}): {drivers_response.status_code}")
                drivers_response.raise_for_status()
            
            for driver in session_drivers:
                drivers.add((driver["driver_number"], driver["full_name"]))
        
        print(drivers)
        
        for driver_number, full_name in drivers:
            practice_1 = None
            practice_2 = None
            practice_3 = None
            sprint_quali = None
            sprint_race = None
            qualifying = None
            race = None
            for session in sessions:
                session_key = session["session_key"]
                print(f"Fetching position for driver {driver_number} ({full_name}) in session: {session_key} ({race_name})")
                position_response = requests.get(endpoint + f"position?session_key={session_key}&driver_number={driver_number}")
                if position_response.status_code == 200:
                    position = position_response.json()
                else:
                    print(f"Failed to fetch position for driver {driver_number} ({full_name}) in session {session_key} ({race_name}): {position_response.status_code}")
                    position_response.raise_for_status()
                
                if not position:
                    continue
                if session["session_name"] == "Practice 1":
                    practice_1 = position[-1]["position"]
                elif session["session_name"] == "Practice 2":
                    practice_2 = position[-1]["position"]
                elif session["session_name"] == "Practice 3":
                    practice_3 = position[-1]["position"]
                elif session["session_name"] == "Sprint Shootout":
                    sprint_quali = position[-1]["position"]
                elif session["session_name"] == "Sprint":
                    sprint_race = position[-1]["position"]
                elif session["session_name"] == "Qualifying":
                    qualifying = position[-1]["position"]
                elif session["session_name"] == "Race":
                    race = position[-1]["position"]
            df = df._append({"meeting_key": meeting_key, "race_name": race_name, "driver_number": driver_number, "driver_name": full_name, "practice_1": practice_1, "practice_2": practice_2, "practice_3": practice_3, "sprint_quali": sprint_quali, "sprint_race": sprint_race, "qualifying": qualifying, "race": race}, ignore_index=True)
    df.to_csv("data.csv", index=False)
    print("Data update process completed successfully")
