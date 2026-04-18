import random
from collections import deque

# Create grid with random obstacles
def create_grid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.choice([1, 1, 1, 0]))  # More free cells (1)
        grid.append(row)
    return grid

# Print Matrix
def print_grid(grid):
    print("\nGenerated N x N Matrix:")
    for row in grid:
        print(row)

# BFS traversal
def bfs(grid, start, goal):
    n = len(grid)
    queue = deque([start])
    visited = set([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            print("Goal Reached!")
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # Check FREE cell (1)
                if grid[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    print("No Path Found")
    return False

# MAIN
n = int(input("Enter Grid Size N: "))
grid = create_grid(n)
print_grid(grid)

sx = int(input("Enter Start X: "))
sy = int(input("Enter Start Y: "))
gx = int(input("Enter Goal X: "))
gy = int(input("Enter Goal Y: "))

start = (sx, sy)
goal = (gx, gy)

# Ensure start and goal are free (1)
grid[sx][sy] = 1
grid[gx][gy] = 1

bfs(grid, start, goal)