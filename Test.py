import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
X = np.array([[1, 2], [1, 4], [3, 4], [5, 6], [5, 8], [7, 8]])

# KMeans model
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Cluster centers
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red')
plt.show()