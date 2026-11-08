# SLIP 17, 18

# Write a Python program to implement Decision Tree classifier model on data
# which is extracted from images that were taken from genuine and forged
# banknote-like specimens.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "banknotes.csv"
)

df.columns = [
    'Variance',
    'Skewness',
    'Curtosis',
    'Entropy',
    'Class'
]

print(df.head())

X = df.drop('Class', axis=1)

y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# print("Predictions:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

new_data = pd.DataFrame(
    [[3.5, 8.2, -2.4, -0.5]],
    columns=['Variance', 'Skewness', 'Curtosis', 'Entropy']
)

prediction = model.predict(new_data)

if prediction[0] == 0:
    print("Banknote Class: Genuine")
else:
    print("Banknote Class: Forged")