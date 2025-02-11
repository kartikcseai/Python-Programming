# example : diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return 30.

def diagonal_sum(matrix):
    n = len(matrix)
    total_sum = 0
    for i in range(n):
        total_sum += matrix[i][i]  # Primary diagonal
        total_sum += matrix[i][n - i - 1]  # Secondary diagonal
    # If matrix has an odd dimension, subtract the center element added twice
    if n % 2 == 1:
        total_sum -= matrix[n // 2][n // 2]
    return total_sum

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = diagonal_sum(matrix)
print(output)
