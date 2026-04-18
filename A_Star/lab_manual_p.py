from collections import defaultdict
import heapq

# -----------------------------
# Graph (Adjacency List)
# -----------------------------
graph = {
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('S', 6), ('E', 6)],
    'B': [('S', 5), ('E', 6), ('D', 7)],
    'C': [('S', 10), ('D', 6)],
    'E': [('A', 6), ('B', 6), ('F', 4)],
    'D': [('B', 7), ('C', 6), ('F', 6)],
    'F': [('E', 4), ('D', 6), ('G', 3)],
    'G': []
}


h = {
    'S': 17,
    'A': 10,
    'B': 13,
    'C': 4,
    'D': 2,
    'E': 4,
    'F': 1,
    'G': 0
}

start = 'S'
goal = 'G'

# -----------------------------
# A* Algorithm
# -----------------------------
open_list = []
heapq.heappush(open_list, (h[start], 0, start))  # (f, g, node)

came_from = {}
g_cost = {start: 0}

step = 0



while open_list:
    step += 1

    # Sort-like view of OPEN list
    temp = sorted(open_list)
    print(f"Step {step} OPEN LIST:")
    for f, g, node in temp:
        print(f"  Node: {node}, g={g}, h={h[node]}, f={f}")
    print()

    f, g, current = heapq.heappop(open_list)

    # Goal check
    if current == goal:
        print("Goal reached!")
        break

    for neighbor, cost in graph[current]:
        new_g = g + cost

        if neighbor not in g_cost or new_g < g_cost[neighbor]:
            g_cost[neighbor] = new_g
            f = new_g + h[neighbor]
            heapq.heappush(open_list, (f, new_g, neighbor))
            came_from[neighbor] = current


path = []
node = goal

while node in came_from:
    path.append(node)
    node = came_from[node]

path.append(start)
path.reverse()

print("\nShortest Path:", " -> ".join(path))
print("Total Cost:", g_cost[goal])