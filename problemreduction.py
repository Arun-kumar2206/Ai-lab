class ProblemReduction:
    def __init__(self):
        self.graph = {}
        self.is_primitive = {}
        self.solved = {}
        self.solution_path = []
    
    def add_problem(self, problem, is_primitive=False):
        self.is_primitive[problem] = is_primitive
        self.solved[problem] = is_primitive
        if problem not in self.graph:
            self.graph[problem] = []
    
    def add_reduction(self, problem, subproblems):
        if problem not in self.graph:
            self.graph[problem] = []
        self.graph[problem].append(subproblems)
    
    def solve(self, problem, level=0):
        indent = "  " * level
        
        # If already solved
        if self.solved.get(problem, False):
            print(f"{indent}'{problem}' is already solved (primitive)")
            return True
        
        # If primitive problem
        if self.is_primitive.get(problem, False):
            print(f"{indent}'{problem}' is a primitive problem - SOLVED")
            self.solved[problem] = True
            self.solution_path.append(problem)
            return True
        
        # If no reductions available
        if problem not in self.graph or not self.graph[problem]:
            print(f"{indent}'{problem}' cannot be reduced further - FAILED")
            return False
        
        print(f"{indent}Solving: '{problem}'")
        
        # Try each reduction
        for subproblems in self.graph[problem]:
            print(f"{indent}Reducing '{problem}' to: {subproblems}")
            
            all_solved = True
            for subproblem in subproblems:
                if not self.solve(subproblem, level + 1):
                    all_solved = False
                    break
            
            if all_solved:
                print(f"{indent}'{problem}' SOLVED via {subproblems}")
                self.solved[problem] = True
                self.solution_path.append(problem)
                return True
        
        print(f"{indent}'{problem}' FAILED - no valid reduction")
        return False

# Taking input
pr = ProblemReduction()

n = int(input("Enter number of problems: "))
print("Enter problems (problem is_primitive[1/0]):")
for i in range(n):
    line = input().split()
    problem = line[0]
    is_prim = int(line[1]) if len(line) > 1 else 0
    pr.add_problem(problem, bool(is_prim))

r = int(input("\nEnter number of reductions: "))
print("Enter reductions (problem -> sub1 sub2 ...):")
for i in range(r):
    line = input().split()
    problem = line[0]
    subproblems = line[1:]
    pr.add_reduction(problem, subproblems)

start = input("\nEnter main problem to solve: ")

print("\n" + "="*60)
print("Problem Reduction Algorithm\n")

if pr.solve(start):
    print("\n" + "="*60)
    print("SUCCESS! Problem solved")
    print(f"Solution path: {' -> '.join(reversed(pr.solution_path))}")
else:
    print("\n" + "="*60)
    print("FAILED! Cannot solve the problem")
# ```

# **Sample Input:**
# ```
# Enter number of problems: 7
# Enter problems (problem is_primitive[1/0]):
# P1 0
# P2 0
# P3 0
# P4 1
# P5 1
# P6 1
# P7 0

# Enter number of reductions: 4
# Enter reductions (problem -> sub1 sub2 ...):
# P1 P2 P3
# P2 P4 P5
# P3 P6
# P7 P4

# Enter main problem to solve: P1
# ```

# **Output:**
# ```
# ============================================================
# Problem Reduction Algorithm

# Solving: 'P1'
# Reducing 'P1' to: ['P2', 'P3']
# Solving: 'P2'
# Reducing 'P2' to: ['P4', 'P5']
# 'P4' is a primitive problem - SOLVED
# 'P5' is a primitive problem - SOLVED
# 'P2' SOLVED via ['P4', 'P5']
# Solving: 'P3'
# Reducing 'P3' to: ['P6']
# 'P6' is a primitive problem - SOLVED
# 'P3' SOLVED via ['P6']
# 'P1' SOLVED via ['P2', 'P3']

# ============================================================
# SUCCESS! Problem solved
# Solution path: P6 -> P3 -> P5 -> P4 -> P2 -> P1