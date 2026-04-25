def dls_find_path(graph, current, target, remaining, visited_path):
    if remaining == 0 and current == target:
        return visited_path
    if remaining > 0:
        for next_node in graph[current]:
            if next_node not in visited_path:
                result = dls_find_path(graph, next_node, target,
                                       remaining - 1, visited_path + [next_node])
                if result:
                    return result
    return None
 
def find_path_iddfs(graph, source, target, max_d):
    for depth in range(max_d + 1):
        found = dls_find_path(graph, source, target, depth, [source])
        if found:
            return found
    return None
 
# Graph Input
graph = {}
n = int(input("Enter total nodes: "))
for _ in range(n):
    node = input("Node: ")
    neighbors = input("Neighbors: ").split()
    graph[node] = neighbors
src = input("Start: ")
dest = input("Destination: ")
depth = int(input("Max depth: "))
path = find_path_iddfs(graph, src, dest, depth)
print("Path:", path) if path else print("No route found")
