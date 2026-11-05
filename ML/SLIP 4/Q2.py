# SLIP 4, 19

# Write a Python program to implement logistic Regression. Use dataset crash.csv is an accident survivor’s dataset portal for the USA hosted by data.gov. The dataset contains passengers' age and speed of vehicle (mph) at the time of impact, and fate of passengers (1 for survived and 0 for not survived) after a crash. Use logistic regression to decide if the age and speed can predict the survivability of the passengers.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("crash.csv")

print(df.head())

print(df.columns)

X = df[['age', 'speed']]
y = df['fate']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = pd.DataFrame({
    'age': [25],
    'speed': [110]
})

predictions = model.predict(new_data)

print("New Predictions:", predictions)

if predictions == 1:
    print("Passenger Survived")
else:
    print("Passenger Not Survived")