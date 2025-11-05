import random
import math

def simulated_annealing(objective_func, initial_solution, temp=1000, cooling_rate=0.95, min_temp=1):
    current_solution = initial_solution
    current_cost = objective_func(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    
    while temp > min_temp:
        # Generate neighbor solution (small random change)
        neighbor = current_solution + random.uniform(-1, 1)
        neighbor_cost = objective_func(neighbor)
        
        # Calculate cost difference
        delta = neighbor_cost - current_cost
        
        # Accept better solution or worse with probability
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution = neighbor
            current_cost = neighbor_cost
            
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
        
        # Cool down
        temp *= cooling_rate
    
    return best_solution, best_cost

# Example: Minimize f(x) = (x - 3)^2
def objective(x):
    return (x - 3) ** 2

# Taking input
initial = float(input("Enter initial solution: "))
temp = float(input("Enter initial temperature (e.g., 1000): "))
cooling = float(input("Enter cooling rate (e.g., 0.95): "))

print("\nOptimizing f(x) = (x-3)^2...")
solution, cost = simulated_annealing(objective, initial, temp, cooling)

print(f"Best solution: x = {solution:.4f}")
print(f"Minimum cost: {cost:.4f}")
# ```

# **Sample Input:**
# ```
# Enter initial solution: 10
# Enter initial temperature (e.g., 1000): 1000
# Enter cooling rate (e.g., 0.95): 0.95
# ```

# **Output:**
# ```
# Optimizing f(x) = (x-3)^2...
# Best solution: x = 3.0021
# Minimum cost: 0.0000