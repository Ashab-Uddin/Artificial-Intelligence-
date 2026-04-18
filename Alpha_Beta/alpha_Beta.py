import math

def alphabeta(curDepth, nodeIndex, isMax, scores, targetDepth, alpha, beta):

    # Base case: leaf node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    # MAX player
    if isMax:
        best = -float('inf')

        # Left child
        val = alphabeta(curDepth + 1, nodeIndex * 2, False,
                        scores, targetDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        # Pruning
        if beta <= alpha:
            return best

        # Right child
        val = alphabeta(curDepth + 1, nodeIndex * 2 + 1, False,
                        scores, targetDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        return best

    # MIN player
    else:
        best = float('inf')

        # Left child
        val = alphabeta(curDepth + 1, nodeIndex * 2, True,
                        scores, targetDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        # Pruning
        if beta <= alpha:
            return best

        # Right child
        val = alphabeta(curDepth + 1, nodeIndex * 2 + 1, True,
                        scores, targetDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        return best


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of leaf nodes (power of 2): "))

scores = []
print("Enter leaf node values:")
for i in range(n):
    scores.append(int(input(f"Score for leaf {i}: ")))

treeDepth = int(math.log2(n))

alpha = float('-inf')
beta = float('inf')

result = alphabeta(0, 0, True, scores, treeDepth, alpha, beta)

print("\nThe optimal value is:", result)