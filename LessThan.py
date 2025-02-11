# Write a function lessthan(lst, k) to return list of numbers less than k from a list lst. The function must use list comprehension. Example: lessthan([1, -2, 0, 5, -3], 0) returns [-2, -3].

def lessthan(lst, k):
    return [x for x in lst if x < k]

# Test cases
print(lessthan([1, -2, 0, 5, -3], 0))  # Output: [-2, -3]
print(lessthan([10, 20, 30, 5, 3], 15))  # Output: [10, 5, 3]
print(lessthan([-5, -10, 0, 8], -3))  # Output: [-5, -10]
print(lessthan([2, 4, 6, 8], 5))  # Output: [2, 4]
print(lessthan([], 5))  # Output: []
