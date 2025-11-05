from itertools import permutations

def tsp(graph, start=0):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    
    min_path = float('inf')
    best_route = []
    
    for perm in permutations(vertices):
        current_cost = 0
        k = start
        route = [start]
        
        for vertex in perm:
            current_cost += graph[k][vertex]
            route.append(vertex)
            k = vertex
        
        current_cost += graph[k][start]  # Return to start
        route.append(start)
        
        if current_cost < min_path:
            min_path = current_cost
            best_route = route
    
    return min_path, best_route

# Taking input from user
n = int(input("Enter number of cities: "))
print("Enter cost matrix (row by row):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting city (0-indexed): "))

min_cost, route = tsp(graph, start)
print(f"\nMinimum cost: {min_cost}")
print(f"Best route: {' -> '.join(map(str, route))}")
# ```

# **Sample Input:**
# ```
# Enter number of cities: 4
# Enter cost matrix (row by row):
# 0 10 15 20
# 10 0 35 25
# 15 35 0 30
# 20 25 30 0
# Enter starting city (0-indexed): 0
# ```

# **Output:**
# ```
# Minimum cost: 80
# Best route: 0 -> 1 -> 3 -> 2 -> 0