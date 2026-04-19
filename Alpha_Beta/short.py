import math

def get_leaves(nodeIndex, depth, targetDepth):
    """Return all leaf values under a node"""
    start = nodeIndex * (2 ** (targetDepth - depth))
    end = start + (2 ** (targetDepth - depth))
    return scores[start:end]


def alphabeta(curDepth, nodeIndex, isMax, scores, targetDepth, alpha, beta):

    # Leaf node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if isMax:
        best = float('-inf')

        # Left child
        val = alphabeta(curDepth+1, nodeIndex*2, False, scores, targetDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        # Pruning check
        if beta <= alpha:
            pruned_values = get_leaves(nodeIndex*2+1, curDepth+1, targetDepth)
            print(f"Pruned RIGHT subtree at node {nodeIndex*2+1} with values {pruned_values}")
            return best

        # Right child
        val = alphabeta(curDepth+1, nodeIndex*2+1, False, scores, targetDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        return best

    else:
        best = float('inf')

        # Left child
        val = alphabeta(curDepth+1, nodeIndex*2, True, scores, targetDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        # Pruning check
        if beta <= alpha:
            pruned_values = get_leaves(nodeIndex*2+1, curDepth+1, targetDepth)
            print(f"Pruned RIGHT subtree at node {nodeIndex*2+1} with values {pruned_values}")
            return best

        # Right child
        val = alphabeta(curDepth+1, nodeIndex*2+1, True, scores, targetDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        return best


# -------- MAIN --------
n = int(input("Enter number of leaf nodes (power of 2): "))

scores = []
print("Enter leaf node values:")
for i in range(n):
    scores.append(int(input(f"Score for leaf {i}: ")))

treeDepth = int(math.log2(n))

result = alphabeta(0, 0, True, scores, treeDepth, float('-inf'), float('inf'))

print("Optimal value:", result)