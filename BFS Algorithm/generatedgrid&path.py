import random
from collections import deque

def print_grid(grid):
    print("\nGenerated N x N Matrix:")
    for row in grid:
        print(row)

def bfs_with_moves(grid, start, goal):
    n = len(grid)
    queue = deque([start])
    visited = set([start])

    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            print("\n Goal Reached!")
            return True

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # Check FREE cell (1)
                if grid[nx][ny] == 1 and (nx, ny) not in visited:
                    print(f" Moving {move} -> ({nx}, {ny})")
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    print("No Path Found")
    return False

# MAIN
n = int(input("Enter Grid Size N: "))
grid = []
print("Enter the grid value: ")
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
print_grid(grid)

sx = int(input("Enter Start X: "))
sy = int(input("Enter Start Y: "))
gx = int(input("Enter Goal X: "))
gy = int(input("Enter Goal Y: "))

# Input validation (important for exam
if not (0 <= sx < n and 0 <= sy < n and 0 <= gx < n and 0 <= gy < n):
    print("Invalid coordinates!")
else:
    start = (sx, sy)
    goal = (gx, gy)

    # Ensure start and goal are free (1)
    grid[sx][sy] = 1
    grid[gx][gy] = 1

    bfs_with_moves(grid, start, goal)