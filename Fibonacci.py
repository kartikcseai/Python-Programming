# Write Python code snippet to display n terms of Fibonacci series using recursion.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:

         return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci(n - 1)  # Recursively get the previous series
        series.append(series[-1] + series[-2])  # Add the next term
        return series

# Example usage:
n = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci(n))
