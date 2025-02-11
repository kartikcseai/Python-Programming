#Write a Python function, (s, x, k), that takes as argument a sequence s and integers x, k (k>0). The function returns True if there are at most k occurrences of x in s. Otherwise it returns False. For example : 
# searchMany ([10, 17, 15, 12], 15, 1) returns True
# searchMany ([10, 12, 12, 12], 12, 2) returns False
# searchMany ([10, 12, 15, 11], 17, 18) returns True

def searchMany(s, x, k):
    return s.count(x) <= k  # Count occurrences and check condition

# Test cases
print(searchMany([10, 17, 15, 12], 15, 1))  # True
print(searchMany([10, 12, 12, 12], 12, 2))  # False
print(searchMany([10, 12, 15, 11], 17, 18)) # True
