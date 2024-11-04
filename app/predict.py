import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score


data = pd.read_csv("data.csv")

data = data.dropna(subset=['race'])

X = data[["race_name", "driver_number", "practice_1", "practice_2", "practice_3", "sprint_quali", "sprint_race", "qualifying"]]
y = data['race']

X = pd.get_dummies(X, columns=['driver_number', 'race_name'])

imputer = SimpleImputer(strategy='mean')
X[['practice_1', 'practice_2', 'practice_3', 'sprint_quali', 'sprint_race', 'qualifying']] = imputer.fit_transform(X[['practice_1', 'practice_2', 'practice_3', 'sprint_quali', 'sprint_race', 'qualifying']])

X['practice_avg'] = X[['practice_1', 'practice_2', 'practice_3']].mean(axis=1)
X['practice_best'] = X[['practice_1', 'practice_2', 'practice_3']].min(axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#i want csv file with the current data the model is using X and y
X.to_csv("X.csv", index=False)

model = RandomForestClassifier(class_weight='balanced', max_depth=4, max_features='sqrt', min_samples_leaf=13, min_samples_split=5, n_estimators=300, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

# print(f"Mean Squared Error: {mse}")
# print(f"R2 Score: {r2}")
print(f"Accuracy: {accuracy}")