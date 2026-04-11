def isSafe(v, graph, color, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graphColorUtil(graph, m, color, v):
    # Base case: all vertices colored
    if v == len(graph):
        return True

    # Try all colors
    for c in range(1, m + 1):
        if isSafe(v, graph, color, c):
            color[v] = c

            if graphColorUtil(graph, m, color, v + 1):
                return True

            color[v] = 0  # Backtrack

    return False


def graphColoring(graph, m):
    V = len(graph)
    color = [0] * V
    #color_names = ["Red", "Green", "Blue", "Yellow", "Orange"]
    #color_names input from user
    color_names = input("Enter color names: ").split()

    #validation
    if len(color_names)<m:
        print("Not enough color name")
        return

    result = graphColorUtil(graph, m, color, 0)
    if result == False:
        print("No solution exists")
        return

    print("Solution exists:")
    print("Assigned colors:")
    for i in range(V):
        print(f"Vertex {i} → {color_names[color[i]-1]}")


# Run
V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

m = int(input("Enter number of colors: "))

graphColoring(graph, m)