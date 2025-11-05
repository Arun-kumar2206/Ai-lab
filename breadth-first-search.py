from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Taking input from user
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for i in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))
print(f"\nBFS starting from vertex {start}:")
g.bfs(start)
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
# Output: BFS starting from vertex 2: 2 0 3 1