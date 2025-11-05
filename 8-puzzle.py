import heapq
import copy

class PuzzleSolver:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
    
    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    val = state[i][j]
                    for gi in range(3):
                        for gj in range(3):
                            if self.goal[gi][gj] == val:
                                distance += abs(i - gi) + abs(j - gj)
        return distance
    
    def get_blank_pos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    
    def get_neighbors(self, state):
        neighbors = []
        i, j = self.get_blank_pos(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = copy.deepcopy(state)
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(new_state)
        
        return neighbors
    
    def solve(self):
        heap = [(self.manhattan_distance(self.initial), 0, self.initial, [self.initial])]
        visited = set()
        
        while heap:
            _, cost, current, path = heapq.heappop(heap)
            
            if current == self.goal:
                return path
            
            state_tuple = tuple(tuple(row) for row in current)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            
            for neighbor in self.get_neighbors(current):
                h = self.manhattan_distance(neighbor)
                g = cost + 1
                f = g + h
                heapq.heappush(heap, (f, g, neighbor, path + [neighbor]))
        
        return None
    
    def print_state(self, state):
        for row in state:
            print(' '.join(map(str, row)))
        print()

# Input
print("Enter initial state (3x3, use 0 for blank):")
initial = [list(map(int, input().split())) for _ in range(3)]

print("\nEnter goal state (3x3, use 0 for blank):")
goal = [list(map(int, input().split())) for _ in range(3)]

solver = PuzzleSolver(initial, goal)
print("\nSolving using A* algorithm...")
solution = solver.solve()

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
# Enter initial state (3x3, use 0 for blank):
# 1 2 3
# 4 6 0
# 7 5 8

# Enter goal state (3x3, use 0 for blank):
# 1 2 3
# 4 5 6
# 7 8 0
# ```

# **Output:**
# ```
# Solving using A* algorithm...
# Solution found in 3 moves:

# Step 0:
# 1 2 3
# 4 6 0
# 7 5 8

# Step 1:
# 1 2 3
# 4 0 6
# 7 5 8

# Step 2:
# 1 2 3
# 4 5 6
# 7 0 8

# Step 3:
# 1 2 3
# 4 5 6
# 7 8 0