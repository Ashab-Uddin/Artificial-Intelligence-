from collections import deque

# Node class
class Node:
    def __init__(self, x, y, level):
        self.x = x          # row position
        self.y = y          # column position
        self.level = level  # distance from source


# BFS function
def bfs(graph, source, goal):
    N = len(graph)

    # 4 direction movement (Down, Up, Right, Left)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Create queue and push source node
    queue = deque()
    queue.append(source)

    # BFS loop
    while queue:
        u = queue.popleft()

        # Explore all 4 directions
        for dx, dy in directions:
            vx = u.x + dx
            vy = u.y + dy

            # Check boundary and valid cell
            if 0 <= vx < N and 0 <= vy < N and graph[vx][vy] == 1:

                level = u.level + 1

                # Check goal
                if vx == goal.x and vy == goal.y:
                    print("Goal found")
                    print("Number of moves =", level)
                    return

                # Mark visited
                graph[vx][vy] = 0

                # Add new node to queue
                queue.append(Node(vx, vy, level))

    # If goal not found
    print("Goal not reachable")


# 🔷 Main function

graph = [
    [0,0,1,0,1],
    [0,1,1,1,1],
    [0,1,0,0,1],
    [1,1,0,1,1],
    [1,0,0,0,1]
]

# Source and Goal
source = Node(0, 2, 0)
goal = Node(4, 4, 0)

# Run BFS
bfs(graph, source, goal)