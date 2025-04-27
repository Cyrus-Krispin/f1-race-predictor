import fastf1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

#starting with first race of 2025 (australian GP)


session_2025_1 = fastf1.get_session(2025, 1, "R")
session_2025_1.load()

laps_2025_1 = session_2025_1.laps[["Driver", "LapTime"]].copy()

laps_2025_1 = laps_2025_1[laps_2025_1['Driver'] == "VER"]

laps_2025_1.to_csv("new.csv")


