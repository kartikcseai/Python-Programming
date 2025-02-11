# write a python program to count the occurence of each element in a list.
from collections import Counter

def count_occurrences(elements):
    occurrences = Counter(elements)  # Count occurrences of each element
    return occurrences

# Example usage:
input_list = input("Enter elements separated by spaces: ").split()
occurrence_dict = count_occurrences(input_list)

print("Occurrences of elements:")
for element, count in occurrence_dict.items():
    print(f"{element}: {count}")
