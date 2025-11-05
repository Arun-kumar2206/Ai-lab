from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dls(self, node, goal, limit, visited, path, level=0):
        """Depth Limited Search helper"""
        if node == goal:
            return True, path + [node]
        
        if level >= limit:
            return False, []
        
        visited.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                found, result_path = self.dls(neighbor, goal, limit, visited, path + [node], level + 1)
                if found:
                    return True, result_path
        
        visited.remove(node)
        return False, []
    
    def iddfs(self, start, goal, max_depth):
        print(f"Iterative Deepening DFS from '{start}' to '{goal}'")
        print("="*60)
        
        for depth in range(max_depth + 1):
            print(f"\nDepth Limit: {depth}")
            print("-"*40)
            
            visited = set()
            found, path = self.dls(start, goal, depth, visited, [])
            
            if found:
                print(f"Goal '{goal}' found at depth {depth}!")
                print("="*60)
                return depth, path
            else:
                print(f"Goal not found at depth {depth}")
        
        print("\n" + "="*60)
        print(f"Goal '{goal}' not found within max depth {max_depth}")
        return -1, []

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for i in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

print("\n")
depth, path = g.iddfs(start, goal, max_depth)

if path:
    print(f"\nOptimal Path: {' -> '.join(path)}")
    print(f"Solution Depth: {depth}")
    print(f"Path Length: {len(path) - 1}")
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
# G H

# Enter start node: A
# Enter goal node: H
# Enter maximum depth: 5
# ```

# **Output:**
# ```
# Iterative Deepening DFS from 'A' to 'H'
# ============================================================

# Depth Limit: 0
# ----------------------------------------
# Goal not found at depth 0

# Depth Limit: 1
# ----------------------------------------
# Goal not found at depth 1

# Depth Limit: 2
# ----------------------------------------
# Goal not found at depth 2

# Depth Limit: 3
# ----------------------------------------
# Goal 'H' found at depth 3!
# ============================================================

# Optimal Path: A -> B -> E -> H
# Solution Depth: 3
# Path Length: 3