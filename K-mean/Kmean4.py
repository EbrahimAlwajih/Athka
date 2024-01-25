import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Generating a random dataset
np.random.seed(0)
X = np.random.rand(100, 2)


# Applying k-Means
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(X)

# Getting the cluster centers
centroids = kmeans.cluster_centers_

# Predicting the cluster for each data point
labels = kmeans.predict(X)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.5)
plt.title("k-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
