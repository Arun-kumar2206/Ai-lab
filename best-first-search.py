import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = {}
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def set_heuristic(self, node, h_value):
        self.heuristic[node] = h_value
    
    def best_first_search(self, start, goal):
        visited = set()
        heap = [(self.heuristic.get(start, 0), start, [start])]
        
        while heap:
            h_val, current, path = heapq.heappop(heap)
            
            if current in visited:
                continue
            
            visited.add(current)
            print(f"Visiting: {current} (h={h_val})")
            
            if current == goal:
                return path
            
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    h = self.heuristic.get(neighbor, 0)
                    heapq.heappush(heap, (h, neighbor, path + [neighbor]))
        
        return None

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for i in range(n):
    u, v = input().split()
    g.add_edge(u, v)

print("\nEnter heuristic values:")
h_count = int(input("Enter number of nodes with heuristic: "))
for i in range(h_count):
    node, h_val = input("Node HeuristicValue: ").split()
    g.set_heuristic(node, int(h_val))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

print(f"\nBest First Search from {start} to {goal}:\n")
path = g.best_first_search(start, goal)

if path:
    print(f"\nPath found: {' -> '.join(path)}")
else:
    print("\nNo path found!")
# ```

# **Sample Input:**
# ```
# Enter number of edges: 7
# Enter edges (u v):
# A B
# A C
# B D
# B E
# C F
# C G
# E H

# Enter heuristic values:
# Enter number of nodes with heuristic: 8
# Node HeuristicValue: A 7
# Node HeuristicValue: B 6
# Node HeuristicValue: C 4
# Node HeuristicValue: D 5
# Node HeuristicValue: E 3
# Node HeuristicValue: F 6
# Node HeuristicValue: G 2
# Node HeuristicValue: H 0

# Enter start node: A
# Enter goal node: H
# ```

# **Output:**
# ```
# Best First Search from A to H:

# Visiting: A (h=7)
# Visiting: C (h=4)
# Visiting: G (h=2)
# Visiting: B (h=6)
# Visiting: E (h=3)
# Visiting: H (h=0)

# Path found: A -> B -> E -> H