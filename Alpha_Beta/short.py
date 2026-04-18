import math

def alphabeta(depth, index, isMax, scores, maxDepth, alpha, beta):

    if depth == maxDepth:
        return scores[index]

    if isMax:
        value = max(
            alphabeta(depth+1, index*2, False, scores, maxDepth, alpha, beta),
            alphabeta(depth+1, index*2+1, False, scores, maxDepth, alpha, beta)
        )
        return value

    else:
        value = min(
            alphabeta(depth+1, index*2, True, scores, maxDepth, alpha, beta),
            alphabeta(depth+1, index*2+1, True, scores, maxDepth, alpha, beta)
        )
        return value


n = int(input())
scores = [int(input()) for _ in range(n)]
depth = int(math.log2(n))

print(alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))