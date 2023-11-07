def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens_util(board, row + 1, N, solutions)

def solve_n_queens(N):
    solutions = []
    solve_n_queens_util([-1] * N, 0, N, solutions)
    return solutions

# Example usage
N = 4  # Change N to solve for a different board size
solutions = solve_n_queens(N)
print("Solutions for", N, "queens problem:")
for solution in solutions:
    print(solution)
