# SLIP 11, 13

# Write a Python program to implement K-means clustering model and classify the
# employees into various income groups or clusters. Preprocess data if require (i.e.
# drop missing or null values). Use the Elbow method and Silhouette Score to find
# the value of k.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("income.csv")

print(df.head())

df = df.dropna()

X = df[['Income']]

sc = StandardScaler()

X = sc.fit_transform(X)

wcss = []

for k in range(1, 6):

    model = KMeans(n_clusters=k, random_state=42)

    model.fit(X)

    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker='o')

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.title("Elbow Method")

plt.show()

for k in range(2, 6):

    model = KMeans(n_clusters=k, random_state=42)

    labels = model.fit_predict(X)

    print(k, silhouette_score(X, labels))

model = KMeans(n_clusters=3, random_state=42)

df['Cluster'] = model.fit_predict(X)

print(df)

plt.scatter(df['Income'], df['Cluster'], c=df['Cluster'])

plt.xlabel("Income")

plt.ylabel("Cluster")

plt.title("Employee Income Groups")

plt.show()

