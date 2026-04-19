def isSafe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graphColorUtil(graph, m, color, v, color_names, solutions):
    # Base case: all vertices colored
    if v == len(graph):
        solutions[0] += 1
        print(f"\nSolution {solutions[0]}:")
        for i in range(len(graph)):
            print(f"Vertex {i} → {color_names[color[i]-1]}")
        return

    # Try all colors
    for c in range(1, m + 1):
        if isSafe(v, graph, color, c):
            color[v] = c

            # Recur to assign colors to next vertex
            graphColorUtil(graph, m, color, v + 1, color_names, solutions)

            color[v] = 0  # Backtrack


def graphColoring(graph, m):
    V = len(graph)
    color = [0] * V

    color_names = input("Enter color names: ").split()

    # Validation
    if len(color_names) < m:
        print("Not enough color names")
        return

    solutions = [0]  # mutable counter

    graphColorUtil(graph, m, color, 0, color_names, solutions)

    if solutions[0] == 0:
        print("No solution exists")
    else:
        print(f"\nTotal solutions: {solutions[0]}")


# Run
V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

graphColoring(graph, m)
