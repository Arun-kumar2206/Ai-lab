import random

def hill_climbing(objective_func, initial, step_size=0.1, max_iterations=1000):
    current = initial
    current_value = objective_func(current)
    path = [(current, current_value)]
    
    print(f"Initial: x = {current:.4f}, f(x) = {current_value:.4f}\n")
    
    for i in range(max_iterations):
        # Generate neighbors
        neighbors = [
            current + step_size,
            current - step_size
        ]
        
        # Evaluate neighbors
        neighbor_values = [(n, objective_func(n)) for n in neighbors]
        
        # Find best neighbor
        best_neighbor, best_value = max(neighbor_values, key=lambda x: x[1])
        
        print(f"Iteration {i+1}: x = {current:.4f}, f(x) = {current_value:.4f}")
        
        # If no improvement, stop
        if best_value <= current_value:
            print(f"\nLocal maximum reached!")
            break
        
        # Move to best neighbor
        current = best_neighbor
        current_value = best_value
        path.append((current, current_value))
    
    return current, current_value, path

# Example objective functions
def func1(x):
    return -(x - 3) ** 2 + 10  # Maximum at x=3

def func2(x):
    import math
    return -x**2 + 4*x  # Maximum at x=2

# Taking input
print("Select objective function:")
print("1. f(x) = -(x-3)^2 + 10")
print("2. f(x) = -x^2 + 4x")
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    objective = func1
else:
    objective = func2

initial = float(input("Enter initial value: "))
step_size = float(input("Enter step size (e.g., 0.1): "))
max_iter = int(input("Enter max iterations: "))

print("\n" + "="*50)
print("Hill Climbing Algorithm\n")

solution, value, path = hill_climbing(objective, initial, step_size, max_iter)

print("\n" + "="*50)
print(f"Final Solution: x = {solution:.4f}")
print(f"Maximum value: f(x) = {value:.4f}")
# ```

# **Sample Input:**
# ```
# Select objective function:
# 1. f(x) = -(x-3)^2 + 10
# 2. f(x) = -x^2 + 4x
# Enter choice (1 or 2): 1
# Enter initial value: 0
# Enter step size (e.g., 0.1): 0.5
# Enter max iterations: 20
# ```

# **Output:**
# ```
# ==================================================
# Hill Climbing Algorithm

# Initial: x = 0.0000, f(x) = 1.0000

# Iteration 1: x = 0.0000, f(x) = 1.0000
# Iteration 2: x = 0.5000, f(x) = 3.7500
# Iteration 3: x = 1.0000, f(x) = 6.0000
# Iteration 4: x = 1.5000, f(x) = 7.7500
# Iteration 5: x = 2.0000, f(x) = 9.0000
# Iteration 6: x = 2.5000, f(x) = 9.7500
# Iteration 7: x = 3.0000, f(x) = 10.0000

# Local maximum reached!

# ==================================================
# Final Solution: x = 3.0000
# Maximum value: f(x) = 10.0000