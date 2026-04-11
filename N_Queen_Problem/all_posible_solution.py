def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# store all solutions here
solutions = []

def solve(board, col, N):
    if col == N:
        # deep copy solution store
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col, N):

            board[row][col] = 1
            solve(board, col + 1, N)
            board[row][col] = 0  # BACKTRACK


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()


# ---------------- MAIN ----------------
N = int(input("Enter N (number of queens): "))

board = [[0 for _ in range(N)] for _ in range(N)]

solve(board, 0, N)

# show results
if len(solutions) == 0:
    print("No solution exists")
else:
    print(f"Total solutions: {len(solutions)}\n")

    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        print_board(sol)