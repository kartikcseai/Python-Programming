# Construct a function ret smaller(1) that returns smallest list from a nested list. If 7 two lists have same length then return the first list that is encountered. For example:
# ret smaller([ [-2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) returns [3,4,5]
# ret smaller([[ -2, -1, 0, 0.12, 1, 2], ['a', 'b', 'c', 'd', 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) returns [6, 7, 8, 9, 10]

def ret_smaller(l):
    return min(l, key=len)  # Find the list with the smallest length

# Test cases
print(ret_smaller([[-2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
# Output: [3, 4, 5]

print(ret_smaller([[-2, -1, 0, 0.12, 1, 2], ['a', 'b', 'c', 'd', 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
# Output: [6, 7, 8, 9, 10]
