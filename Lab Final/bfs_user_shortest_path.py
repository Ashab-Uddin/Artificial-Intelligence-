
from collections import deque


def print_grid(grid):
    print("\nGenerated Grid:")
    for row in grid:
        print(row)

def bfs_with_parent(grid, start, goal):
    n = len(grid)
    queue = deque([start])
    visited = set([start])
    parent = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return parent

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                # Check FREE cell (1)
                if grid[nx][ny] == 1 and (nx, ny) not in visited:
                    print(f"➡️ Moving -> ({nx}, {ny})")
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None

# Recursive path printing
def print_path(parent, start, goal):
    if parent is None:
        print("No Path Found")
        return

    if goal == start:
        print(start)
        return

    print_path(parent, start, parent[goal])
    print(goal)

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

start = (sx, sy)
goal = (gx, gy)

# Ensure start and goal are free (1)
grid[sx][sy] = 1
grid[gx][gy] = 1

parent = bfs_with_parent(grid, start, goal)

print("\nFinal Shortest Path:")
print_path(parent, start, goal)