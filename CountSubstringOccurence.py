# write a function count_substring() that takes a string and a substring as input and returns the number of times the substring occurs in the string. 
# example: count_substring("abababa", "aba") should return 3.

def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

# Example usage
input_string = "abababa"
substring = "aba"
output = count_substring(input_string, substring)
print(output)
