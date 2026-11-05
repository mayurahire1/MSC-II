# Repeated Slips : 3, 20

# Q.2 Write a Python program to implement multiple Linear Regression for predicting house price.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("housearea2.csv")

print(df.head())

X = df[['area', 'bedroom', 'age']]

y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LinearRegression()

model.fit(X_train, y_train)

new_house = pd.DataFrame({
    'area': [3500],
    'bedroom': [3],
    'age': [20]
})

result = model.predict(new_house)

print("Predicted House Price:", result[0])