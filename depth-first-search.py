from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=' ')
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        
        return visited

# Taking input from user
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for i in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))
print(f"\nDFS starting from vertex {start}:")
g.dfs(start)
# ```

# **Sample Input:**
# ```
# Enter number of edges: 6
# Enter edges (u v):
# 0 1
# 0 2
# 1 2
# 2 0
# 2 3
# 3 3
# Enter starting vertex: 2
# Output: DFS starting from vertex 2: 2 0 1 3