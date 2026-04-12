import math

# ---------------- MINIMAX ----------------
def minimax(depth, node_index, is_max, values, max_depth, counter):
    counter["visited"] += 1

    if depth == max_depth:
        return values[node_index]

    if is_max:
        left_val = minimax(depth + 1, node_index * 2, False, values, max_depth, counter)
        right_val = minimax(depth + 1, node_index * 2 + 1, False, values, max_depth, counter)
        return max(left_val, right_val)
    else:
        left_val = minimax(depth + 1, node_index * 2, True, values, max_depth, counter)
        right_val = minimax(depth + 1, node_index * 2 + 1, True, values, max_depth, counter)
        return min(left_val, right_val)


# ---------------- ALPHA-BETA ----------------
def alpha_beta(depth, node_index, is_max, values, max_depth, alpha, beta, counter):
    counter["visited"] += 1

    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -math.inf

        best = max(best, alpha_beta(depth + 1, node_index * 2, False,
                                    values, max_depth, alpha, beta, counter))
        alpha = max(alpha, best)

        if alpha >= beta:
            nodes_to_prune = 2 ** (max_depth - depth - 1)
            counter["pruned"] += nodes_to_prune
            return best

        best = max(best, alpha_beta(depth + 1, node_index * 2 + 1, False,
                                    values, max_depth, alpha, beta, counter))
        return best

    else:
        best = math.inf

        best = min(best, alpha_beta(depth + 1, node_index * 2, True,
                                    values, max_depth, alpha, beta, counter))
        beta = min(beta, best)

        if alpha >= beta:
            nodes_to_prune = 2 ** (max_depth - depth - 1)
            counter["pruned"] += nodes_to_prune
            return best

        best = min(best, alpha_beta(depth + 1, node_index * 2 + 1, True,
                                    values, max_depth, alpha, beta, counter))
        return best


# ---------------- MAIN ----------------
def main():
    values = list(map(int, input("Enter leaf node values (space separated): ").split()))

    n = len(values)

    if (n & (n - 1)) != 0:
        print("Number of leaf nodes must be a power of 2!")
        return

    max_depth = int(math.log2(n))

    print("\nleaf node values:", values)

    # -------- MINIMAX --------
    print("\nRunning Minimax...")
    minimax_counter = {"visited": 0}
    minimax_result = minimax(0, 0, True, values, max_depth, minimax_counter)

    print("Nodes evaluated (Minimax):", minimax_counter["visited"])
    print("Optimal value:", minimax_result)

    # -------- ALPHA-BETA --------
    print("\nRunning Alpha-Beta Pruning...")
    alpha_beta_counter = {"visited": 0, "pruned": 0}
    alpha_beta_result = alpha_beta(0, 0, True, values, max_depth,
                                   -math.inf, math.inf, alpha_beta_counter)

    print("Nodes evaluated (Alpha-Beta):", alpha_beta_counter["visited"])
    print("Nodes pruned:", alpha_beta_counter["pruned"])
    print("Optimal value:", alpha_beta_result)

    # -------- EFFICIENCY --------
    improvement = ((minimax_counter["visited"] - alpha_beta_counter["visited"])
                   / minimax_counter["visited"]) * 100

    print("\nEfficiency improvement: {:.2f}%".format(improvement))


if __name__ == "__main__":
    main()