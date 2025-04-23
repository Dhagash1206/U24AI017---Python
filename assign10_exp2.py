"""Write a program to place the queens randomly in the chess board so that all the conditions
are satisfied. Find the solutions to the problem."""

import random

def is_valid(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def random_8_queen_solution():
    attempts = 0
    while True:
        board = list(range(8))
        random.shuffle(board) 
        attempts += 1
        if is_valid(board):
            return board, attempts
        
        
solution, tries = random_8_queen_solution()
print("Found a valid 8-Queens solution after", tries, "attempts:")
print("Board representation (row: column):")
for row, col in enumerate(solution):
    print(f"Row {row}: Column {col}")
