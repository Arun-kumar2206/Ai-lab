class PuzzleSolver:
    def __init__(self):
        self.state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j
    
    def move(self, direction):
        i, j = self.find_blank()
        moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        
        if direction in moves:
            di, dj = moves[direction]
            ni, nj = i + di, j + dj
            
            if 0 <= ni < 3 and 0 <= nj < 3:
                self.state[i][j], self.state[ni][nj] = self.state[ni][nj], self.state[i][j]
            else:
                print("Invalid move!")
    
    def display(self):
        for row in self.state:
            print(' '.join(str(x) if x != 0 else '_' for x in row))
        print()
    
    def is_solved(self):
        return self.state == self.goal
    
    def play(self):
        print("8-Puzzle Game")
        print("Controls: w=up, s=down, a=left, d=right, q=quit\n")
        
        while True:
            self.display()
            
            if self.is_solved():
                print("Puzzle solved!")
                break
            
            move = input("Move: ").lower()
            if move == 'q':
                break
            self.move(move)
            print()

PuzzleSolver().play()