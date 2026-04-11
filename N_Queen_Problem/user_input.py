def is_safe(board, row, col, N):
    # Check left side in same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, N):
    # Base case: all queens placed
    if col == N:
        return True

    for row in range(N):
        if is_safe(board, row, col, N):

            board[row][col] = 1  # place queen

            if solve(board, col + 1, N):
                return True

            board[row][col] = 0  # BACKTRACK

    return False


def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# ---------------- MAIN ----------------
N = int(input("Enter N (number of queens): "))

board = [[0 for _ in range(N)] for _ in range(N)]

if solve(board, 0, N):
    print("\nSolution Found:\n")
    print_board(board, N)
else:
    print("No solution exists")