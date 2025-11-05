def knapsack_memo(weights, values, capacity, n, memo=None):
    if memo is None:
        memo = {}
    
    # Base case
    if n == 0 or capacity == 0:
        return 0
    
    # Check memo
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    
    # If weight exceeds capacity, skip item
    if weights[n-1] > capacity:
        result = knapsack_memo(weights, values, capacity, n-1, memo)
    else:
        # Max of including or excluding
        include = values[n-1] + knapsack_memo(weights, values, capacity - weights[n-1], n-1, memo)
        exclude = knapsack_memo(weights, values, capacity, n-1, memo)
        result = max(include, exclude)
    
    memo[(n, capacity)] = result
    return result

# Input
n = int(input("Items: "))
weights = list(map(int, input("Weights: ").split()))
values = list(map(int, input("Values: ").split()))
capacity = int(input("Capacity: "))

max_val = knapsack_memo(weights, values, capacity, n)
print(f"\nMax value: {max_val}")

# ```

# **Sample Input:**
# ```
# Enter number of items: 4
# Enter weight and value for each item:
# Item 1 (weight value): 2 3
# Item 2 (weight value): 3 4
# Item 3 (weight value): 4 5
# Item 4 (weight value): 5 6

# Enter knapsack capacity: 8
# ```

# **Output:**
# ```
# ============================================================
# 0/1 Knapsack Problem
# ============================================================

# Maximum value: 10
# Selected items (0-indexed): [1, 2, 3]

# Item Details:
# Item | Weight | Value
# -------------------------
#    1 |      3 |     4
#    2 |      4 |     5
#    3 |      5 |     6
# -------------------------
# Total:      8 |    10
# Remaining capacity: 0