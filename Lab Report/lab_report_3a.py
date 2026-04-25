def depth_limited_search(graph, current, depth_left, seen):
    if depth_left == 0:
        print(current, end=" ")
        return
    seen.add(current)
    for adj in graph[current]:
        if adj not in seen:
            depth_limited_search(graph, adj, depth_left - 1, seen)
 
def run_iddfs(graph, source, limit):
    for d in range(limit + 1):
        print(f"\nLevel {d}:", end=" ")
        seen = set()
        depth_limited_search(graph, source, d, seen)
 
# Graph Input
graph = {}
num_nodes = int(input("How many nodes? "))
for _ in range(num_nodes):
    n = input("Node name: ")
    adj = input("Adjacent nodes (space-separated): ").split()
    graph[n] = adj
src = input("Start node: ")
lim = int(input("Max depth limit: "))
run_iddfs(graph, src, lim)
