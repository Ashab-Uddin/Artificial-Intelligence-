import math

# ---------------- MINIMAX ----------------
def minimax_search(level, index, max_turn, values, depth, stats):
    stats["visited"] += 1

    if level == depth:
        return values[index]

    if max_turn:
        left = minimax_search(level + 1, index * 2, False, values, depth, stats)
        right = minimax_search(level + 1, index * 2 + 1, False, values, depth, stats)
        return max(left, right)
    else:
        left = minimax_search(level + 1, index * 2, True, values, depth, stats)
        right = minimax_search(level + 1, index * 2 + 1, True, values, depth, stats)
        return min(left, right)


# ---------------- ALPHA-BETA ----------------
def alpha_beta_search(level, index, max_turn, values, depth, alpha, beta, stats):
    stats["visited"] += 1

    if level == depth:
        return values[index]

    if max_turn:
        best = -float("inf")

        best = max(best, alpha_beta_search(level + 1, index * 2, False,
                                           values, depth, alpha, beta, stats))
        alpha = max(alpha, best)

        if alpha >= beta:
            stats["pruned"] += 2 ** (depth - level - 1)
            return best

        best = max(best, alpha_beta_search(level + 1, index * 2 + 1, False,
                                           values, depth, alpha, beta, stats))
        return best

    else:
        best = float("inf")

        best = min(best, alpha_beta_search(level + 1, index * 2, True,
                                           values, depth, alpha, beta, stats))
        beta = min(beta, best)

        if alpha >= beta:
            stats["pruned"] += 2 ** (depth - level - 1)
            return best

        best = min(best, alpha_beta_search(level + 1, index * 2 + 1, True,
                                           values, depth, alpha, beta, stats))
        return best


# ---------------- MAIN PROGRAM ----------------
def run_game_tree():
    values = list(map(int, input("Enter leaf node values: ").split()))
    n = len(values)

    if n & (n - 1) != 0:
        print("Input size must be a power of 2!")
        return

    depth = int(math.log2(n))

    print("\nLeaf nodes:", values)

    # Minimax run
    print("\nRunning Minimax...")
    mini_stats = {"visited": 0}
    mini_result = minimax_search(0, 0, True, values, depth, mini_stats)

    print("Nodes visited (Minimax):", mini_stats["visited"])
    print("Optimal value:", mini_result)

    # Alpha-Beta run
    print("\nRunning Alpha-Beta Pruning...")
    ab_stats = {"visited": 0, "pruned": 0}
    ab_result = alpha_beta_search(0, 0, True, values, depth,
                                   -float("inf"), float("inf"), ab_stats)

    print("Nodes visited (Alpha-Beta):", ab_stats["visited"])
    print("Nodes pruned:", ab_stats["pruned"])
    print("Optimal value:", ab_result)

    # Efficiency
    improvement = ((mini_stats["visited"] - ab_stats["visited"])
                   / mini_stats["visited"]) * 100

    print("\nEfficiency improvement: {:.2f}%".format(improvement))


if __name__ == "__main__":
    run_game_tree()