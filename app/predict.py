import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv("data.csv")

X = data[["race_name", "driver_number", "practice_1", "practice_2", "practice_3", "sprint_quali", "sprint_race", "qualifying"]]
y = data['race']

X = pd.get_dummies(X, columns=['driver_number', 'race_name'])

imputer = SimpleImputer(strategy='mean')
X[['practice_1', 'practice_2', 'practice_3', 'sprint_quali', 'sprint_race', 'qualifying']] = imputer.fit_transform(
    X[['practice_1', 'practice_2', 'practice_3', 'sprint_quali', 'sprint_race', 'qualifying']])

X['practice_avg'] = X[['practice_1', 'practice_2', 'practice_3']].mean(axis=1)
X['practice_best'] = X[['practice_1', 'practice_2', 'practice_3']].min(axis=1)

for i in range(1, 4):
    data[f'last_{i}_race'] = data.groupby('driver_number')['race'].shift(i)

data[['last_1_race', 'last_2_race', 'last_3_race']] = imputer.fit_transform(
    data[['last_1_race', 'last_2_race', 'last_3_race']])
X['driver_form'] = data[['last_1_race', 'last_2_race', 'last_3_race']].mean(axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X.to_csv("X.csv", index=False)
y.to_csv("y.csv", index=False)

model = RandomForestClassifier(class_weight='balanced', random_state=42)

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [4, 6, 8],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 3, 5],
    'max_features': ['sqrt', 'log2']
}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', verbose=1, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Accuracy: {accuracy}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': best_model.feature_importances_
}).sort_values(by='Importance', ascending=False)
feature_importances.to_csv("feature_importances.csv", index=False)

print("Feature importances saved to 'feature_importances.csv'.")
