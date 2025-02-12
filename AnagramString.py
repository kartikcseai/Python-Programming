# write a function group_anagrams() that takes a list of strings and group them into list of anagrams (words that have same characters but in different order). 
# For example, given the list ["listen", "silent", "enlist", "bat", "tab", "cat"], 
# the function should return [["listen", "silent", "enlist"], ["bat", "tab"], ["cat"]].

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# Example usage
input_words = ["listen", "silent", "enlist", "bat", "tab", "cat"]
output = group_anagrams(input_words)
print(output)
