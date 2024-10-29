import pandas as pd
import numpy as np
import requests

endpoint = "https://api.openf1.org/v1/"

def get_meetings():
    response = requests.get(endpoint + "meetings")
    return response.json()

def update_all_data():
    df = pd.DataFrame(columns=["meeting_id", "session_id", "race_name", "driver_id", "driver_name", "team_id", "team_name", "practice_1", "practice_2", "practice_3", "sprint_quali", "sprint_race", "race"])
    meetings = get_meetings()
    for meeting in meetings:
        if meeting['meeting_name'] == "Pre-Season Testing":
            continue
        meeting_key = meeting["meeting_key"]
        sessions = requests.get(endpoint + f"sessions?meeting_key={meeting_key}").json()
    print(meetings)