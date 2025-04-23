"""Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
according to the following constraints.
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other."""


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(row, board, solutions):
    if row == 8:
        solutions.append(board[:])
        return
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(row + 1, board, solutions)

def eight_queens():
    solutions = []
    board = [-1] * 8
    solve_n_queens(0, board, solutions)
    return solutions
