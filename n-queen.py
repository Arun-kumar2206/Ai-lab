class NQueenSolver:
    def __init__(self, n=4):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.queens = 0

    def is_safe(self, row, col):
        # Check row and column
        for i in range(self.n):
            if self.board[row][i] == 1 or self.board[i][col] == 1:
                return False
        
        # Check diagonals
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    if abs(i - row) == abs(j - col):
                        return False
        return True

    def place_queen(self, row, col):
        if self.board[row][col] == 1:
            print("Queen already there!")
            return
        
        if self.is_safe(row, col):
            self.board[row][col] = 1
            self.queens += 1
            print("Queen placed!")
        else:
            print("Unsafe position!")

    def display(self):
        print()
        for row in self.board:
            print(" ".join("Q" if x == 1 else "." for x in row))
        print(f"\nQueens placed: {self.queens}/{self.n}")

    def is_solved(self):
        return self.queens == self.n

    def play(self):
        print(f"{self.n}-Queen Problem - Place {self.n} queens safely!")
        print("Enter row and column (0-based), or 'q' to quit\n")
        
        while True:
            self.display()
            
            if self.is_solved():
                print("\nPuzzle solved!")
                break
            
            move = input("\nEnter row col: ").lower()
            if move == 'q':
                break
            
            try:
                row, col = map(int, move.split())
                if 0 <= row < self.n and 0 <= col < self.n:
                    self.place_queen(row, col)
                else:
                    print("Invalid position!")
            except:
                print("Invalid input!")

NQueenSolver().play()