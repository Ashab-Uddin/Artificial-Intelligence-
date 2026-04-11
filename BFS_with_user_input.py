from collections import deque

# Node class
class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level


def bfs(graph, source, goal, N):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = deque()
    queue.append(source)

    while queue:
        u = queue.popleft()

        for dx, dy in directions:
            vx = u.x + dx
            vy = u.y + dy

            # Boundary + valid check
            if 0 <= vx < N and 0 <= vy < N and graph[vx][vy] == 1:

                level = u.level + 1

                # Goal check
                if vx == goal.x and vy == goal.y:
                    print("\n✅ Goal found!")
                    print("Number of moves =", level)
                    return

                graph[vx][vy] = 0  # visited
                queue.append(Node(vx, vy, level))

    print("\n❌ Goal not reachable")


# 🔷 🔵 Main Program (User Input)

# Grid size input
N = int(input("Enter grid size N: "))

print("\nEnter the grid (0 = obstacle, 1 = path):")

graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

# Start position
sx, sy = map(int, input("\nEnter source (row col): ").split())

# Goal position
gx, gy = map(int, input("Enter goal (row col): ").split())

source = Node(sx, sy, 0)
goal = Node(gx, gy, 0)

# Run BFS
bfs(graph, source, goal, N)