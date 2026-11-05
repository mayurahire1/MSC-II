# SLIPS - 5, 6

# Write a Python program to fit the Polynomial Linear Regression
# models to Salary_positions.csv data.
# Also, predict the salaries of level 11 and level 12 employees.

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("position_sal.csv")

df.columns = df.columns.str.strip()

print(df.head())

X = df[['level']]
y = df['salary']

poly = PolynomialFeatures(degree=4)

X_poly = poly.fit_transform(X)

model = LinearRegression()

model.fit(X_poly, y)

level11 = pd.DataFrame({'level': [11]})

level11_poly = poly.transform(level11)

salary11 = model.predict(level11_poly)

print("Level 11 Salary:", salary11[0])


level12 = pd.DataFrame({'level': [12]})

level12_poly = poly.transform(level12)

salary12 = model.predict(level12_poly)

print("Level 12 Salary:", salary12[0])
