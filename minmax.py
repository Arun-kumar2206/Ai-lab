import math

def minimax(depth, node_index, is_maximizing, scores, height):
    # Base case: leaf node
    if depth == height:
        return scores[node_index]
    
    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Input
print("Enter leaf node scores (space-separated):")
scores = list(map(int, input().split()))

height = math.log2(len(scores))
if not height.is_integer():
    print("Number of scores must be power of 2!")
else:
    height = int(height)
    result = minimax(0, 0, True, scores, height)
    
    print(f"\nOptimal value: {result}")
    print("\nGame Tree:")
    print(f"Leaf scores: {scores}")
    print(f"Tree height: {height}")
# ```

# **Sample Input:**
# ```
# Enter leaf node scores (space-separated):
# 3 5 2 9 12 5 23 23
# ```

# **Output:**
# ```
# Optimal value: 12

# Game Tree:
# Leaf scores: [3, 5, 2, 9, 12, 5, 23, 23]
# Tree height: 3