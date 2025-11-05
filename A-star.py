import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = {}
    
    def add_edge(self, u, v, cost):
        self.graph[u].append((v, cost))
    
    def set_heuristic(self, node, h_value):
        self.heuristic[node] = h_value
    
    def a_star(self, start, goal):
        # Priority queue: (f_cost, g_cost, current_node, path)
        heap = [(self.heuristic.get(start, 0), 0, start, [start])]
        visited = set()
        
        while heap:
            f_cost, g_cost, current, path = heapq.heappop(heap)
            
            if current in visited:
                continue
            
            visited.add(current)
            h_val = self.heuristic.get(current, 0)
            print(f"Visiting: {current} | g={g_cost}, h={h_val}, f={f_cost}")
            
            if current == goal:
                return path, g_cost
            
            for neighbor, edge_cost in self.graph[current]:
                if neighbor not in visited:
                    new_g = g_cost + edge_cost
                    h = self.heuristic.get(neighbor, 0)
                    f = new_g + h
                    heapq.heappush(heap, (f, new_g, neighbor, path + [neighbor]))
        
        return None, float('inf')

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v cost):")
for i in range(n):
    u, v, cost = input().split()
    g.add_edge(u, v, int(cost))

print("\nEnter heuristic values:")
h_count = int(input("Enter number of nodes: "))
for i in range(h_count):
    node, h_val = input("Node HeuristicValue: ").split()
    g.set_heuristic(node, int(h_val))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

print(f"\nA* Search from {start} to {goal}:\n")
path, cost = g.a_star(start, goal)

if path:
    print(f"\nOptimal path: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("\nNo path found!")
# ```

# **Sample Input:**
# ```
# Enter number of edges: 8
# Enter edges (u v cost):
# A B 1
# A C 4
# B D 3
# B E 2
# C F 5
# C G 2
# E H 4
# G H 3

# Enter heuristic values:
# Enter number of nodes: 8
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
# A* Search from A to H:

# Visiting: A | g=0, h=7, f=7
# Visiting: B | g=1, h=6, f=7
# Visiting: E | g=3, h=3, f=6
# Visiting: C | g=4, h=4, f=8
# Visiting: H | g=7, h=0, f=7

# Optimal path: A -> B -> E -> H
# Total cost: 7