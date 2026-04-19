
# Print grid
def print_grid(grid):
    print("\nGenerated Grid:")
    for row in grid:
        print(row)

# DFS with parent tracking
def dfs(grid, current, goal, visited, parent):
    n = len(grid)
    x, y = current

    if current == goal:
        return True

    visited.add(current)

    directions = [(-1, 0),
                  (1, 0),
                  (0, -1),
                  (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and (nx, ny) not in visited:
                parent[(nx, ny)] = (x, y)

                if dfs(grid, (nx, ny), goal, visited, parent):
                    return True

    return False

# Recursive path printing
def print_path(parent, start, goal):
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

# Ensure start and goal are free
grid[sx][sy] = 1
grid[gx][gy] = 1

visited = set()
parent = {}

found = dfs(grid, start, goal, visited, parent)

if found:
    print("\nGoal Reached!")
    print("\nPath from Source to Destination:")
    print_path(parent, start, goal)
else:
    print("No Path Found")