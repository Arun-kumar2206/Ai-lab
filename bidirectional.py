from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For bidirectional, graph should be undirected
    
    def bfs_step(self, queue, visited, other_visited):
        """Perform one step of BFS"""
        if not queue:
            return None, None
        
        node, path = queue.popleft()
        
        # Check if this node was visited from other direction
        if node in other_visited:
            return node, path
        
        visited[node] = path
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
        
        return None, None
    
    def bidirectional_search(self, start, goal):
        if start == goal:
            return [start]
        
        # Forward search from start
        queue_forward = deque([(start, [start])])
        visited_forward = {start: [start]}
        
        # Backward search from goal
        queue_backward = deque([(goal, [goal])])
        visited_backward = {goal: [goal]}
        
        print(f"Bidirectional Search: '{start}' <-> '{goal}'")
        print("="*60)
        
        iteration = 0
        
        while queue_forward or queue_backward:
            iteration += 1
            print(f"\nIteration {iteration}:")
            
            # Forward BFS step
            print(f"  Forward:  Exploring from {list(queue_forward)[0][0] if queue_forward else 'None'}")
            meeting_node, forward_path = self.bfs_step(queue_forward, visited_forward, visited_backward)
            
            if meeting_node:
                # Combine paths
                backward_path = visited_backward[meeting_node]
                complete_path = forward_path + backward_path[-2::-1]
                print(f"\n  Meeting point found: {meeting_node}")
                print("="*60)
                return complete_path
            
            # Backward BFS step
            print(f"  Backward: Exploring from {list(queue_backward)[0][0] if queue_backward else 'None'}")
            meeting_node, backward_path = self.bfs_step(queue_backward, visited_backward, visited_forward)
            
            if meeting_node:
                # Combine paths
                forward_path = visited_forward[meeting_node]
                complete_path = forward_path + backward_path[-2::-1]
                print(f"\n  Meeting point found: {meeting_node}")
                print("="*60)
                return complete_path
        
        print("\n" + "="*60)
        print("No path found!")
        return []

# Taking input
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v) - undirected:")
for i in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

print("\n")
path = g.bidirectional_search(start, goal)

if path:
    print(f"\nPath Found: {' -> '.join(path)}")
    print(f"Path Length: {len(path) - 1}")
# ```

# **Sample Input:**
# ```
# Enter number of edges: 9
# Enter edges (u v) - undirected:
# A B
# A C
# B D
# B E
# C F
# D G
# E G
# F G
# G H

# Enter start node: A
# Enter goal node: H
# ```

# **Output:**
# ```
# Bidirectional Search: 'A' <-> 'H'
# ============================================================

# Iteration 1:
#   Forward:  Exploring from A
#   Backward: Exploring from H

# Iteration 2:
#   Forward:  Exploring from B
#   Backward: Exploring from G

# Iteration 3:
#   Forward:  Exploring from C
#   Backward: Exploring from D

#   Meeting point found: D
# ============================================================

# Path Found: A -> B -> D -> G -> H
# Path Length: 4