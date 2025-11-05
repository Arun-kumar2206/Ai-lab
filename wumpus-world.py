from collections import deque

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = [0, 0]
        self.wumpus = None
        self.gold = None
        self.pits = []
        self.visited = set()
        self.safe = set()
        
    def setup_world(self):
        print("Enter Wumpus position (x y): ", end='')
        x, y = map(int, input().split())
        self.wumpus = [x, y]
        
        print("Enter Gold position (x y): ", end='')
        x, y = map(int, input().split())
        self.gold = [x, y]
        
        n = int(input("Enter number of pits: "))
        for i in range(n):
            print(f"Enter pit {i+1} position (x y): ", end='')
            x, y = map(int, input().split())
            self.pits.append([x, y])
    
    def is_safe(self, pos):
        if pos == self.wumpus:
            return False
        if pos in self.pits:
            return False
        if pos[0] < 0 or pos[0] >= self.size or pos[1] < 0 or pos[1] >= self.size:
            return False
        return True
    
    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        return [n for n in neighbors if 0 <= n[0] < self.size and 0 <= n[1] < self.size]
    
    def bfs_find_gold(self):
        queue = deque([[self.agent_pos]])
        visited = {tuple(self.agent_pos)}
        
        while queue:
            path = queue.popleft()
            current = path[-1]
            
            if current == self.gold:
                return path
            
            for neighbor in self.get_neighbors(current):
                if tuple(neighbor) not in visited and self.is_safe(neighbor):
                    visited.add(tuple(neighbor))
                    queue.append(path + [neighbor])
        
        return None
    
    def solve(self):
        print("\nSearching for gold...")
        path = self.bfs_find_gold()
        
        if path:
            print("Path to gold found!")
            print("Agent route:")
            for i, pos in enumerate(path):
                print(f"Step {i}: {pos}")
            print(f"\nTotal steps: {len(path) - 1}")
        else:
            print("No safe path to gold found!")

# Main program
world = WumpusWorld()
world.setup_world()
world.solve()
# ```

# **Sample Input:**
# ```
# Enter Wumpus position (x y): 1 2
# Enter Gold position (x y): 2 3
# Enter number of pits: 2
# Enter pit 1 position (x y): 1 1
# Enter pit 2 position (x y): 3 1
# ```

# **Output:**
# ```
# Searching for gold...
# Path to gold found!
# Agent route:
# Step 0: [0, 0]
# Step 1: [0, 1]
# Step 2: [0, 2]
# Step 3: [0, 3]
# Step 4: [1, 3]
# Step 5: [2, 3]

# Total steps: 5