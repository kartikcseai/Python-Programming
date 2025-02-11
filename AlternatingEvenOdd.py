# Write a Python function, alternating (1st), that takes as argument a sequence 1st. The function returns True if the elements in 1st are alternately odd and even, starting with an even number. Otherwise it returns False. For example:
# alternating ([10, 9, 9, 6]) returns False
# alternating ([10, 15, 8]) returns True
# alternating ([10]) returns True
# alternating ([]) returns True
# alternating ([15, 10, 9]) returns False

def alternating(lst):
    if not lst:  # Empty list case
        return True
    if lst[0] % 2 != 0:  # First element must be even   
        return False
    for i in range(1, len(lst)):  # Check alternating pattern
        if lst[i] % 2 == lst[i - 1] % 2:
            return False
    return True

# Test cases
print(alternating([10, 9, 9, 6]))  # False
print(alternating([10, 15, 8]))     # True
print(alternating([1, 15, 8]))    # False
print(alternating([10]))           # True
print(alternating([]))             # True
print(alternating([15, 10, 9]))    # False
