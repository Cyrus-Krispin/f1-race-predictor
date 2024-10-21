import pandas as pd

driver_details = pd.read_csv("driver_details.csv")
race_details = pd.read_csv("race_details.csv")
fastest_laps = pd.read_csv("fastest_laps_details.csv")
qualifying_details = pd.read_csv("qualifying_details.csv")
practice_1 = pd.read_csv("practice-1_details.csv")
practice_2 = pd.read_csv("practice-2_details.csv")
practice_3 = pd.read_csv("practice-3_details.csv")
pit_stop_summary = pd.read_csv("pit_stop_summary.csv")
starting_positions = pd.read_csv("starting_positions.csv")
team_details = pd.read_csv("team_details.csv")

# Merge all the data
data = race_details.merge(driver_details, on=["Name", "No"])
data = data.merge(fastest_laps, on=["Name", "Race", "No", "Team"])
data = data.merge(qualifying_details, on=["Name", "Race", "No", "Team"])
data = data.merge(practice_1, on=["Name", "Race", "No", "Team"])
data = data.merge(practice_2, on=["Name", "Race", "No", "Team"])
data = data.merge(practice_3, on=["Name", "Race", "No", "Team"])
aggeregate = pit_stop_summary.groupby(["Race", "Team", "Name", "No"]).agg({
    "Pit Stop Lap": lambda x: list(x),
    "Time of Day": lambda x: list(x),
    "Pit Stop Time": lambda x: list(x),
    "Total Pit Stop Time": lambda x: list(x)
}).reset_index()

data = data.merge(aggeregate, on=["Race", "Name", "No", "Team"])
data = data.merge(starting_positions, on=["Race", "Name", "No", "Team"])
data = data.merge(team_details, on=["Short Team Name"])



pd.DataFrame(data=data).to_csv("merged_data.csv", index=False, header=True)