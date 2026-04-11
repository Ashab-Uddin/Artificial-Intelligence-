from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def bfs_path(graph, source, goal, N):
    queue = deque()
    queue.append(source)

    # Visited + Parent dictionary
    visited = [[False]*N for _ in range(N)]
    parent = {}

    visited[source.x][source.y] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        u = queue.popleft()

        # Goal found
        if u.x == goal.x and u.y == goal.y:
            print("✅ Shortest Path Found!")
            path = []

            # Backtracking from goal to source
            curr = (u.x, u.y)
            while curr in parent:
                path.append(curr)
                curr = parent[curr]

            path.append((source.x, source.y))
            path.reverse()

            print("Path:", path)
            print("Moves =", len(path)-1)
            return

        # Explore neighbours
        for dx, dy in directions:
            vx = u.x + dx
            vy = u.y + dy

            if 0 <= vx < N and 0 <= vy < N and graph[vx][vy] == 1 and not visited[vx][vy]:
                visited[vx][vy] = True
                parent[(vx, vy)] = (u.x, u.y)   # store parent
                queue.append(Node(vx, vy))

    print("❌ No path found")


# 🔷 Main

graph = [
    [1,1,1],
    [0,1,0],
    [1,1,1]
]

source = Node(0,0)
goal = Node(2,2)

bfs_path(graph, source, goal, len(graph))