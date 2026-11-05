# SLIP 10, 14

# Q.2 Write a Python program to implement a Naïve Bayes classifier for classification.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")

X = df[['SepalLengthCm', 'SepalWidthCm',
        'PetalLengthCm', 'PetalWidthCm']]

y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("Predictions:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = pd.DataFrame(
    [[3, 2.5, 1.4, 3]],
    columns=['SepalLengthCm', 'SepalWidthCm',
             'PetalLengthCm', 'PetalWidthCm']
)

result = model.predict(new_data)

print("Flower:", result[0])