import math
import copy

HUMAN = 'x'
AI = 'o'
EMPTY = '0'

nodes_evaluated = 0
nodes_pruned = 0


def print_board(board):
    for row in board:
        print(",".join(row))
    print()


def check_winner(b):
    lines = []

    # rows + cols
    for i in range(3):
        lines.append(b[i])
        lines.append([b[0][i], b[1][i], b[2][i]])

    # diagonals
    lines.append([b[0][0], b[1][1], b[2][2]])
    lines.append([b[0][2], b[1][1], b[2][0]])

    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == 3:
            return line[0]

    return None


def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True


def evaluate(board):
    winner = check_winner(board)
    if winner == AI:
        return 10
    elif winner == HUMAN:
        return -10
    return 0


def get_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


def minimax(board, depth, is_max, alpha, beta):
    global nodes_evaluated, nodes_pruned

    score = evaluate(board)
    if score != 0 or is_full(board):
        return score

    if is_max:
        best = -math.inf

        for (i, j) in get_moves(board):
            board[i][j] = AI
            nodes_evaluated += 1

            val = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                nodes_pruned += 1
                break

        return best

    else:
        best = math.inf

        for (i, j) in get_moves(board):
            board[i][j] = HUMAN
            nodes_evaluated += 1

            val = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = EMPTY

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                nodes_pruned += 1
                break

        return best


def best_move(board):
    global nodes_evaluated, nodes_pruned

    best_val = -math.inf
    move = (-1, -1)

    nodes_evaluated = 0
    nodes_pruned = 0

    for (i, j) in get_moves(board):
        board[i][j] = AI
        val = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = EMPTY

        if val > best_val:
            best_val = val
            move = (i, j)

    print("Nodes evaluated:", nodes_evaluated)
    print("Nodes pruned:", nodes_pruned)

    return move


# ---------------- MAIN ----------------

board = []

print("Enter board (3x3):")
for _ in range(3):
    board.append(input().split(","))

print("\nInitial Board:")
print_board(board)

row, col = best_move(board)

board[row][col] = AI

print("AI Move Played:")
print_board(board)