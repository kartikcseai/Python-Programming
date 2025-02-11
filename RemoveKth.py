# Write a Python function removekth(s, k) that takes as input a string s and an integer k>=0 and removes the character at index k. If k is beyond the length of s, the whole of s is returned. For example : 
# removekth("PYTHON", 1) returns "PTHON"
# removekth ("PYTHON", 3) returns "ΡΥΤΟΝ"
# removekth("PYTHON", 0) returns "YTHON"
# removekth("PYTHON", 20) returns "PYTHON"

def removekth(s, k):
    if k < 0 or k >= len(s):  # If k is out of bounds, return the original string
        return s
    return s[:k] + s[k+1:]  # Remove character at index k

# Test cases
print(removekth("PYTHON", 1))  # Output: "PTHON"
print(removekth("PYTHON", 3))  # Output: "PYTON"
print(removekth("PYTHON", 0))  # Output: "YTHON"
print(removekth("PYTHON", 20)) # Output: "PYTHON"
