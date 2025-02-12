# Write Python program to swap two numbers without using Intermediate/Temporary variables. Prompt the user for input.

# Accept user input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping using arithmetic operations
a = a + b
b = a - b
a = a - b

# Display swapped values
print(f"After swapping: a = {a}, b = {b}")
