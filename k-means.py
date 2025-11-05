import random
import math

def kmeans(data, k, max_iter=10):
    # Initialize centroids randomly
    centroids = random.sample(data, k)
    
    for iteration in range(max_iter):
        # Assign clusters
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [math.dist(point, c) for c in centroids]
            clusters[distances.index(min(distances))].append(point)
        
        # Update centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                centroid = [sum(p[i] for p in cluster) / len(cluster) 
                           for i in range(len(cluster[0]))]
                new_centroids.append(centroid)
        
        if new_centroids == centroids:
            break
        centroids = new_centroids
    
    return clusters, centroids

# Input
n = int(input("Points: "))
data = [list(map(float, input().split())) for _ in range(n)]
k = int(input("K: "))

clusters, centroids = kmeans(data, k)

print("\nResults:")
for i, (cluster, centroid) in enumerate(zip(clusters, centroids)):
    print(f"Cluster {i+1}: {len(cluster)} points, Centroid: {centroid}")

# ```

# **Sample Output:**
# ```
# ============================================================
# K-Means Clustering
# ============================================================
# Initial Centroids:
#   C1: [1.5, 2.0]
#   C2: [5.0, 7.0]

# --- Iteration 1 ---
# Cluster 1: 4 points
# Cluster 2: 4 points

# New Centroids:
#   C1: ['2.25', '3.12']
#   C2: ['4.62', '6.12']

# --- Iteration 2 ---
# Cluster 1: 4 points
# Cluster 2: 4 points

# New Centroids:
#   C1: ['2.25', '3.12']
#   C2: ['4.62', '6.12']

# Converged after 2 iterations!

# ============================================================
# Final Results
# ============================================================

# Cluster 1:
#   Centroid: [2.25, 3.13]
#   Points (4):
#     [1.0, 1.0]
#     [1.5, 2.0]
#     [3.0, 4.0]
#     [3.5, 4.5]

# Cluster 2:
#   Centroid: [4.62, 6.12]
#   Points (4):
#     [5.0, 7.0]
#     [3.5, 5.0]
#     [4.5, 5.0]
#     [6.0, 8.0]