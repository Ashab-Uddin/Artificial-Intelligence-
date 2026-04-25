import heapq
 
def astar(graph, heuristic, origin, destination):
    pq = []
    heapq.heappush(pq, (heuristic[origin], origin, [origin], 0))
    visited = set()
 
    while pq:
        print("\n-- Priority Queue --")
        for entry in pq:
            print(entry)
 
        f, node, route, cost_g = heapq.heappop(pq)
 
        if node == destination:
            print("\nDestination reached!")
            print("Path taken:", " -> ".join(route))
            print("Total cost:", cost_g)
            return
 
        if node in visited:
            continue
        visited.add(node)
 
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g_new = cost_g + weight
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(pq, (f_new, neighbor, route + [neighbor], g_new))
 
    print("Path could not be found.")
 
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
 
heuristic = {'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 1, 'F': 0}
 
astar(graph, heuristic, 'A', 'E')
