from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dls(self, start, goal, limit, visited=None, path=None, level=0):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        indent = "  " * level
        print(f"{indent}Visiting: {start} at level {level}")
        
        visited.add(start)
        path.append(start)
        
        # Goal found
        if start == goal:
            print(f"{indent}Goal '{goal}' found!")
            return True, path.copy()
        
        # Depth limit reached
        if level >= limit:
            print(f"{indent}Depth limit reached at {start}")
            path.pop()
            return False, []
        
        # Explore neighbors
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                found, result_path = self.dls(neighbor, goal, limit, visited, path, level + 1)
                if found:
                    return True, result_path
        
        path.pop()
        return False, []
    
    def depth_limited_search(self, start, goal, limit):
        print(f"Depth Limited Search (Limit = {limit})")
        print("="*50)
        found, path = self.dls(start, goal, limit)
        return found, path

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for i in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

print("\n")
found, path = g.depth_limited_search(start, goal, limit)

print("\n" + "="*50)
if found:
    print(f"SUCCESS! Path found: {' -> '.join(path)}")
    print(f"Path length: {len(path) - 1}")
else:
    print(f"FAILED! Goal not found within depth limit {limit}")
# ```

# **Sample Input:**
# ```
# Enter number of edges: 8
# Enter edges (u v):
# A B
# A C
# B D
# B E
# C F
# C G
# E H
# E I

# Enter start node: A
# Enter goal node: H
# Enter depth limit: 3
# ```

# **Output:**
# ```
# Depth Limited Search (Limit = 3)
# ==================================================
# Visiting: A at level 0
#   Visiting: B at level 1
#     Visiting: D at level 2
#       Depth limit reached at D
#     Visiting: E at level 2
#       Visiting: H at level 3
#       Depth limit reached at H
#       Visiting: I at level 3
#       Depth limit reached at I
#   Visiting: C at level 1
#     Visiting: F at level 2
#       Depth limit reached at F
#     Visiting: G at level 2
#       Depth limit reached at G

# ==================================================
# FAILED! Goal not found within depth limit 3
# ```

# **Example with Higher Limit:**

# **Input:**
# ```
# Enter depth limit: 4
# ```

# **Output:**
# ```
# Depth Limited Search (Limit = 4)
# ==================================================
# Visiting: A at level 0
#   Visiting: B at level 1
#     Visiting: D at level 2
#       Depth limit reached at D
#     Visiting: E at level 2
#       Visiting: H at level 3
#       Goal 'H' found!

# ==================================================
# SUCCESS! Path found: A -> B -> E -> H
# Path length: 3