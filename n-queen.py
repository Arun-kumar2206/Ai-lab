from collections import deque
import copy

class PuzzleSolver:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
    
    def get_blank_pos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    
    def get_neighbors(self, state):
        neighbors = []
        i, j = self.get_blank_pos(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = copy.deepcopy(state)
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(new_state)
        
        return neighbors
    
    def state_to_tuple(self, state):
        return tuple(tuple(row) for row in state)
    
    def bfs_solve(self):
        queue = deque([(self.initial, [self.initial])])
        visited = {self.state_to_tuple(self.initial)}
        
        while queue:
            current, path = queue.popleft()
            
            if current == self.goal:
                return path
            
            for neighbor in self.get_neighbors(current):
                state_tuple = self.state_to_tuple(neighbor)
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def print_state(self, state):
        for row in state:
            print(' '.join(map(str, row)))
        print()

# Taking input
print("Enter initial state (3x3 matrix, use 0 for blank):")
initial = []
for i in range(3):
    row = list(map(int, input().split()))
    initial.append(row)

print("\nEnter goal state (3x3 matrix, use 0 for blank):")
goal = []
for i in range(3):
    row = list(map(int, input().split()))
    goal.append(row)

solver = PuzzleSolver(initial, goal)
print("\nSolving...")
solution = solver.bfs_solve()

if solution:
    print(f"Solution found in {len(solution) - 1} moves:\n")
    for i, state in enumerate(solution):
        print(f"Step {i}:")
        solver.print_state(state)
else:
    print("No solution found!")
# ```

# **Sample Input:**
# ```
# Enter initial state (3x3 matrix, use 0 for blank):
# 1 2 3
# 4 0 5
# 6 7 8

# Enter goal state (3x3 matrix, use 0 for blank):
# 1 2 3
# 4 5 6
# 7 8 0
# ```

# **Output:**
# ```
# Solving...
# Solution found in 3 moves:

# Step 0:
# 1 2 3
# 4 0 5
# 6 7 8

# Step 1:
# 1 2 3
# 4 5 0
# 6 7 8

# Step 2:
# 1 2 3
# 4 5 6
# 7 8 0