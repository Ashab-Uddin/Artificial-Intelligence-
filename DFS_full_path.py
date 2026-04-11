# DFS Path Print

def dfs(graph, x, y, goal, path, N):
    # Boundary + obstacle check
    if x < 0 or y < 0 or x >= N or y >= N or graph[x][y] == 0:
        return False

    # Add current node to path
    path.append((x, y))

    # Goal check
    if (x, y) == goal:
        print("✅ Path found:")
        print(path)
        return True

    # Mark visited
    graph[x][y] = 0

    # Explore 4 directions
    if (dfs(graph, x+1, y, goal, path, N) or
        dfs(graph, x-1, y, goal, path, N) or
        dfs(graph, x, y+1, goal, path, N) or
        dfs(graph, x, y-1, goal, path, N)):
        return True

    # Backtracking (important 🔥)
    path.pop()
    return False


# 🔷 Main

graph = [
    [1,1,1],
    [0,1,0],
    [1,1,1]
]

source = (0, 0)
goal = (2, 2)

path = []

if not dfs(graph, source[0], source[1], goal, path, len(graph)):
    print("❌ No path found")