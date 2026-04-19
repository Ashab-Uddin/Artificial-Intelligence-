import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

    # Base case: leaf node reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    # Max player's turn
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )

    # Min player's turn
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )




n = int(input("Enter number of leaf nodes (power of 2): "))

scores = []
print("Enter leaf node values:")
for i in range(n):
    scores.append(int(input(f"Score for leaf {i}: ")))

treeDepth = int(math.log2(n))

result = minimax(0, 0, True, scores, treeDepth)

print("\nThe optimal value is:", result)