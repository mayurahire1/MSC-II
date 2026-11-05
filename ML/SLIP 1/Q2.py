# Repeated Slips : 1, 2

# Write a Python program to reduce 4D data to 2D data using PCA for iris flower dataset. Use Logistic regression and train the model to predict new flowers based on given measurements.

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

pca = PCA(n_components=2)
X = pca.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

result = model.predict([[1.0, 1.0]])

print("Flower:", iris.target_names[result[0]])