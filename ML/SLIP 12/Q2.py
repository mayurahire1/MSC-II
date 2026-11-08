# SLIP 12, 16

# Write a Python program to implement Agglomerative clustering on a synthetic dataset.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("synthetic1.csv")

print(df.head())

X = df[['step', 'amount', 'oldbalanceOrg',
        'newbalanceOrig', 'oldbalanceDest',
        'newbalanceDest']]

X = X.dropna()

# X = X.sample(n=1000, random_state=42)

sc = StandardScaler()

X_scaled = sc.fit_transform(X)

model = AgglomerativeClustering(n_clusters=3)

labels = model.fit_predict(X_scaled)

print("Cluster Labels:")

# print(labels)

plt.scatter(X['amount'], X['oldbalanceOrg'], c=labels)

plt.xlabel("Amount")

plt.ylabel("Old Balance")

plt.title("Agglomerative Clustering")

plt.show()