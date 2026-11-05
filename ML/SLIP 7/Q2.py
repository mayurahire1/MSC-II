
# SLIPS - 7, 8

# Write a Python program to classify the Iris flowers dataset using SVM
# and find out the flower type depending on the given input data.
# Find the accuracy of all SVM kernels.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv("Iris.csv")

print(df.head())

X = df[['SepalLengthCm', 'SepalWidthCm',
        'PetalLengthCm', 'PetalWidthCm']]

y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

kernels = ['linear', 'poly', 'rbf', 'sigmoid']

for k in kernels:

    model = SVC(kernel=k)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(k, "Accuracy:",
          accuracy_score(y_test, y_pred))

model = SVC(kernel='linear')

model.fit(X_train, y_train)

new = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=['SepalLengthCm', 'SepalWidthCm',
             'PetalLengthCm', 'PetalWidthCm']
)

new_scaled = sc.transform(new)

result = model.predict(new_scaled)

print("Flower:", result[0])