# write a function that returns the prime factors of a given number. 
#exapmle: prime_factors(36) should return [2, 2, 3, 3].
# prime_factors(56) should return [2, 2, 2, 7].

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Example usage
n = 56
output = prime_factors(n)
print(output)
