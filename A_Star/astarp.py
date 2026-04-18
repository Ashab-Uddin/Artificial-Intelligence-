import heapq

class Node:
    def __init__(self, name, g, h, parent=None):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


def print_open_list(pq, step):
    print(f"\nStep {step} OPEN LIST:")
    
    # sort for display (without modifying actual queue)
    temp = sorted(pq, key=lambda x: x.f)
    
    for node in temp:
        print(f"  Node: {node.name}, g={node.g}, h={node.h}, f={node.f}")


def a_star():
    # Graph using dictionary (like your example S, A, B...)
    graph = {
        'S': {'A': 6, 'B': 5, 'C': 10},
        'A': {'D': 1},
        'B': {'E': 6},
        'C': {'D': 6},
        'D': {'G': 2},
        'E': {'F': 4},
        'F': {'G': 3},
        'G': {}
    }

    # Heuristic values
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

    pq = []
    heapq.heappush(pq, Node(start, 0, h[start]))

    step = 1

    print("--- A* Search Steps ---")

    while pq:
        print_open_list(pq, step)

        current = heapq.heappop(pq)

        if current.name == goal:
            print("\nGoal reached!")

            # reconstruct path
            path = []
            temp = current
            while temp:
                path.append(temp.name)
                temp = temp.parent

            path.reverse()

            print("\nShortest Path:", " -> ".join(path))
            print("Total Cost:", current.g)
            return

        # expand neighbors
        for neighbor, cost in graph[current.name].items():
            child = Node(
                neighbor,
                current.g + cost,
                h[neighbor],
                current
            )
            heapq.heappush(pq, child)

        step += 1


# Run
a_star()