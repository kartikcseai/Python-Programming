# Write a program to check an input number is prime or not. 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Accept user input
num = int(input("Enter a number: "))

# Check and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
