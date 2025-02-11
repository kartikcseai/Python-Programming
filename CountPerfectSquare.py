#Write a Python program, countSquares(N), that returns the count of perfect squares less than or equal to N (N>1).

import math

def countSquares(N):
    if N <= 1:
        return 0  # There are no perfect squares ≤ 1
    return int(math.sqrt(N))  # The number of perfect squares ≤ N

# Test cases
print(countSquares(10))  # Output: 3 (1, 4, 9)
print(countSquares(25))  # Output: 5 (1, 4, 9, 16, 25)
print(countSquares(50))  # Output: 7 (1, 4, 9, 16, 25, 36, 49)
print(countSquares(1))   # Output: 1 (only 1 is a perfect square)
print(countSquares(2))
print(countSquares(0))# Output: 0 (no perfect squares)
