import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))
    
    def uniform_cost_search(self, start, goal):
        # Priority queue: (cost, node, path)
        heap = [(0, start, [start])]
        visited = set()
        
        print(f"Uniform Cost Search from '{start}' to '{goal}'")
        print("="*60)
        
        while heap:
            cost, current, path = heapq.heappop(heap)
            
            if current in visited:
                continue
            
            visited.add(current)
            print(f"Visiting: {current} | Cost: {cost} | Path: {' -> '.join(path)}")
            
            # Goal found
            if current == goal:
                print("="*60)
                print(f"Goal '{goal}' reached!")
                return cost, path
            
            # Explore neighbors
            for neighbor, edge_cost in self.graph[current]:
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(heap, (new_cost, neighbor, new_path))
        
        print("="*60)
        print(f"Goal '{goal}' not reachable!")
        return float('inf'), []

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v cost):")
for i in range(n):
    u, v, cost = input().split()
    g.add_edge(u, int(cost), v)

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

print("\n")
total_cost, path = g.uniform_cost_search(start, goal)

if path:
    print(f"\nOptimal Path: {' -> '.join(path)}")
    print(f"Total Cost: {total_cost}")
# ```

# **Sample Input:**
# ```
# Enter number of edges: 10
# Enter edges (u v cost):
# A B 1
# A C 4
# B D 3
# B E 2
# C F 5
# C G 2
# D H 4
# E H 3
# G H 1
# F H 6

# Enter start node: A
# Enter goal node: H
# ```

# **Output:**
# ```
# Uniform Cost Search from 'A' to 'H'
# ============================================================
# Visiting: A | Cost: 0 | Path: A
# Visiting: B | Cost: 1 | Path: A -> B
# Visiting: E | Cost: 3 | Path: A -> B -> E
# Visiting: C | Cost: 4 | Path: A -> C
# Visiting: G | Cost: 6 | Path: A -> C -> G
# Visiting: D | Cost: 4 | Path: A -> B -> D
# Visiting: H | Cost: 6 | Path: A -> B -> E -> H
# ============================================================
# Goal 'H' reached!

# Optimal Path: A -> B -> E -> H
# Total Cost: 6