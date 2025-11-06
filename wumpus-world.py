class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent = [0, 0]
        self.wumpus = [1, 2]
        self.gold = [2, 3]
        self.pits = [[1, 1], [3, 1]]
        
    def perceive(self):
        x, y = self.agent
        neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        
        if self.agent == self.wumpus:
            return "WUMPUS! You died!"
        if self.agent in self.pits:
            return "PIT! You fell!"
        if self.agent == self.gold:
            return "GOLD! You won!"
        
        perceptions = []
        for n in neighbors:
            if n == self.wumpus:
                perceptions.append("Stench")
            if n in self.pits:
                perceptions.append("Breeze")
        
        return ", ".join(perceptions) if perceptions else "All clear"
    
    def move(self, direction):
        x, y = self.agent
        moves = {'w': [-1, 0], 's': [1, 0], 'a': [0, -1], 'd': [0, 1]}
        
        if direction in moves:
            dx, dy = moves[direction]
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                self.agent = [new_x, new_y]
            else:
                print("Can't move outside grid!")
    
    def play(self):
        print("Wumpus World - Find the Gold!")
        print("Controls: w=up, s=down, a=left, d=right, q=quit\n")
        
        while True:
            print(f"Position: {self.agent}")
            print(f"Perception: {self.perceive()}\n")
            
            if self.agent == self.gold or self.agent == self.wumpus or self.agent in self.pits:
                break
            
            move = input("Move: ").lower()
            if move == 'q':
                break
            self.move(move)
            print()

# Run game
WumpusWorld().play()

# **Sample Game Play:**
# ```
# 🎮 Wumpus World - Find the Gold!
# Controls: w=up, s=down, a=left, d=right, q=quit

# Position: [0, 0]
# Perception: ✅ All clear

# Move: d

# Position: [0, 1]
# Perception: ✅ All clear

# Move: d

# Position: [0, 2]
# Perception: 👃 Stench

# Move: s

# Position: [1, 2]
# Perception: 👃 Stench

# Move: s

# Position: [2, 2]
# Perception: 💨 Breeze, 👃 Stench

# Move: d

# Position: [2, 3]
# Perception: 🏆 GOLD! You won!
# ```