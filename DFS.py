# Node class
class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth


found = False   # global variable


def dfs(graph, u, goal, N):
    global found

    # Mark visited
    graph[u.x][u.y] = 0

    # 4 direction (Down, Up, Right, Left)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        vx = u.x + dx
        vy = u.y + dy

        # Boundary + valid check
        if 0 <= vx < N and 0 <= vy < N and graph[vx][vy] == 1:

            depth = u.depth + 1
            print(f"Move to ({vx}, {vy})")

            # Goal check
            if vx == goal.x and vy == goal.y:
                print("Goal found")
                print("Moves =", depth)
                found = True
                return

            # Recursive call
            dfs(graph, Node(vx, vy, depth), goal, N)

            # Stop if goal found
            if found:
                return


# 🔷 Main অংশ

graph = [
    [0,0,1,0,1],
    [0,1,1,1,1],
    [0,1,0,0,1],
    [1,1,0,1,1],
    [1,0,0,0,1]
]

N = len(graph)

source = Node(0, 2, 0)
goal = Node(4, 4, 0)

dfs(graph, source, goal, N)

if not found:
    print("Goal not reachable")