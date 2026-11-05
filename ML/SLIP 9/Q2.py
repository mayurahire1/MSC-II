# SLIP 9, 15

# Write a Python program to implement the K-Nearest Neighbors ML algorithm to
# build a prediction model. (Use Iris Dataset / Salary dataset)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")

X = df[['SepalLengthCm', 'SepalWidthCm',
        'PetalLengthCm', 'PetalWidthCm']]

y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("Predictions:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = pd.DataFrame(
    [[3, 2.5, 3.4, 1]],
    columns=['SepalLengthCm', 'SepalWidthCm',
             'PetalLengthCm', 'PetalWidthCm']
)

new = sc.transform(new_data)

result = model.predict(new)

print("Flower:", result[0])