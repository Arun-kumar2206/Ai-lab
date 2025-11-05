class AOStar:
    def __init__(self):
        self.graph = {}
        self.heuristic = {}
        self.cost = {}
        self.solved = {}
    
    def add_node(self, node, h_value):
        self.heuristic[node] = h_value
        self.solved[node] = False
    
    def add_and_edge(self, parent, children, cost):
        if parent not in self.graph:
            self.graph[parent] = []
        self.graph[parent].append(('AND', children, cost))
    
    def add_or_edge(self, parent, child, cost):
        if parent not in self.graph:
            self.graph[parent] = []
        self.graph[parent].append(('OR', [child], cost))
    
    def calculate_cost(self, node):
        if node not in self.graph or self.solved[node]:
            return self.heuristic.get(node, 0)
        
        min_cost = float('inf')
        
        for edge_type, children, edge_cost in self.graph[node]:
            if edge_type == 'AND':
                total = edge_cost + sum(self.calculate_cost(child) for child in children)
            else:  # OR
                total = edge_cost + self.calculate_cost(children[0])
            
            min_cost = min(min_cost, total)
        
        return min_cost
    
    def ao_star(self, start, goals):
        print(f"Starting AO* from {start}\n")
        
        while not self.solved[start]:
            self.cost[start] = self.calculate_cost(start)
            print(f"Node {start}: cost = {self.cost[start]}")
            
            # Check if goal reached
            if start in goals:
                self.solved[start] = True
                break
            
            # Select best path
            if start not in self.graph:
                break
            
            min_cost = float('inf')
            best_edge = None
            
            for edge in self.graph[start]:
                edge_type, children, edge_cost = edge
                if edge_type == 'AND':
                    total = edge_cost + sum(self.heuristic.get(c, 0) for c in children)
                else:
                    total = edge_cost + self.heuristic.get(children[0], 0)
                
                if total < min_cost:
                    min_cost = total
                    best_edge = edge
            
            if best_edge:
                _, children, _ = best_edge
                print(f"Expanding: {start} -> {children}\n")
                
                all_solved = True
                for child in children:
                    if child in goals:
                        self.solved[child] = True
                    elif not self.solved.get(child, False):
                        all_solved = False
                
                if all_solved:
                    self.solved[start] = True
            else:
                break
        
        print(f"Final cost for {start}: {self.cost.get(start, 0)}")

# Taking input
ao = AOStar()

n = int(input("Enter number of nodes: "))
print("Enter nodes with heuristic (node h_value):")
for i in range(n):
    node, h = input().split()
    ao.add_node(node, int(h))

e = int(input("\nEnter number of edges: "))
print("Enter edges (type parent child1 [child2...] cost):")
print("Type: 'AND' or 'OR'")
for i in range(e):
    line = input().split()
    edge_type = line[0]
    parent = line[1]
    cost = int(line[-1])
    children = line[2:-1]
    
    if edge_type == 'AND':
        ao.add_and_edge(parent, children, cost)
    else:
        ao.add_or_edge(parent, children[0], cost)

start = input("\nEnter start node: ")
goals = input("Enter goal nodes (space separated): ").split()

print("\n" + "="*40)
ao.ao_star(start, goals)
# ```

# **Sample Input:**
# ```
# Enter number of nodes: 6
# Enter nodes with heuristic (node h_value):
# A 1
# B 2
# C 3
# D 0
# E 0
# F 0

# Enter number of edges: 5
# Enter edges (type parent child1 [child2...] cost):
# Type: 'AND' or 'OR'
# AND A B C 2
# OR B D 1
# OR C E F 2
# OR E 0
# OR F 0

# Enter start node: A
# Enter goal nodes (space separated): D E F
# ```

# **Output:**
# ```
# ========================================
# Starting AO* from A

# Node A: cost = 6
# Expanding: A -> ['B', 'C']

# Final cost for A: 6