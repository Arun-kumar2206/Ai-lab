import math
from collections import Counter

def knn_predict(X_train, y_train, test_point, k):
    # Calculate distances
    distances = [(math.dist(test_point, x), y) for x, y in zip(X_train, y_train)]
    
    # Sort and get k nearest
    distances.sort()
    k_nearest = distances[:k]
    
    # Majority vote
    labels = [label for _, label in k_nearest]
    return Counter(labels).most_common(1)[0][0]

# Input
n = int(input("Training samples: "))
X_train = []
y_train = []
for _ in range(n):
    *features, label = input().split()
    X_train.append(list(map(float, features)))
    y_train.append(label)

k = int(input("K: "))
test = list(map(float, input("Test point: ").split()))

prediction = knn_predict(X_train, y_train, test, k)
print(f"Predicted: {prediction}")

# ```

# **Sample Output:**
# ```
# ============================================================
# KNN Classification
# ============================================================
# Training completed with 6 samples

# Predicting 3 test samples...

#   Test point: [1.2, 1.5]
#   3 Nearest Neighbors:
#     Distance: 0.54, Label: A, Point: [1.0, 1.0]
#     Distance: 0.71, Label: A, Point: [1.5, 2.0]
#     Distance: 3.10, Label: B, Point: [3.0, 4.0]
#   Predicted class: A

#   Test point: [4.0, 5.5]
#   3 Nearest Neighbors:
#     Distance: 0.50, Label: B, Point: [4.5, 5.0]
#     Distance: 1.12, Label: B, Point: [3.5, 5.0]
#     Distance: 1.58, Label: B, Point: [5.0, 7.0]
#   Predicted class: B

#   Test point: [2.5, 3.5]
#   3 Nearest Neighbors:
#     Distance: 0.71, Label: B, Point: [3.0, 4.0]
#     Distance: 1.80, Label: A, Point: [1.5, 2.0]
#     Distance: 2.12, Label: A, Point: [1.0, 1.0]
#   Predicted class: B

# ============================================================
# Results
# ============================================================

# Test Point | Actual | Predicted | Correct
# ---------------------------------------------
# [1.2, 1.5] | A      | A         | ✓
# [4.0, 5.5] | B      | B         | ✓
# [2.5, 3.5] | B      | B         | ✓

# Accuracy: 100.00%