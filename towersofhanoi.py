def tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        moves[0] += 1
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
    
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    moves[0] += 1
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)

# Taking input
n = int(input("Enter number of disks: "))

print(f"\nSolution for {n} disks:\n")
moves = [0]
tower_of_hanoi(n, 'A', 'C', 'B', moves)

print(f"\nTotal moves: {moves[0]}")
print(f"Formula: 2^n - 1 = {2**n - 1}")
# ```

# **Sample Input:**
# ```
# Enter number of disks: 3
# ```

# **Output:**
# ```
# Solution for 3 disks:

# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C

# Total moves: 7
# Formula: 2^n - 1 = 7