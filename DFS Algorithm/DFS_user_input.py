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

    # 4 directions
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

            # Recursive DFS call
            dfs(graph, Node(vx, vy, depth), goal, N)

           
            if found:
                return


# 🔷 Main (User Input)

N = int(input("Enter grid size: "))

print("Enter grid (0 = block, 1 = path):")
graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

sx, sy = map(int, input("Enter source (row col): ").split())
gx, gy = map(int, input("Enter goal (row col): ").split())

source = Node(sx, sy, 0)
goal = Node(gx, gy, 0)

dfs(graph, source, goal, N)

if not found:
    print("❌ Goal not reachable")