# write a python function file_stats(filename) that reads a text file and calculates the following statistics. 
# 1- total number of lines. 
# 2- Total number of words. 
# 3- total number of character(no whitespaces). 
# 4- Total of vowels. 
# 5- Total number of consonants. 
# 6- Total number of special characters. 
# 7- Total number of digits. 
 
import string
def file_stats(filename):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"
    special_chars = string.punctuation
    
    total_lines = 0
    total_words = 0
    total_chars = 0
    total_vowels = 0
    total_consonants = 0
    total_special_chars = 0
    total_digits = 0
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            total_lines += 1
            words = line.split()
            total_words += len(words)
            
            for char in line:
                if char.isalpha():
                    if char in vowels:
                        total_vowels += 1
                    elif char in consonants:
                        total_consonants += 1
                elif char in digits:
                    total_digits += 1
                elif char in special_chars:
                    total_special_chars += 1
                if not char.isspace():
                    total_chars += 1
    
    stats = {
        "Total Lines": total_lines,
        "Total Words": total_words,
        "Total Characters (No Whitespaces)": total_chars,
        "Total Vowels": total_vowels,
        "Total Consonants": total_consonants,
        "Total Special Characters": total_special_chars,
        "Total Digits": total_digits
    }
    
    return stats



# only for option 1-4
# def file_stats(filename):
#     vowels = set("AEIOUaeiou")  # Set of vowels
#     total_lines = total_words = total_chars = total_vowels = 0

#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             total_lines += 1
#             words = line.split()
#             total_words += len(words)
#             total_chars += sum(len(word) for word in words)  # Excluding whitespaces
#             total_vowels += sum(1 for char in line if char in vowels)

#     return {
#         "Total Lines": total_lines,
#         "Total Words": total_words,
#         "Total Characters (no spaces)": total_chars,
#         "Total Vowels": total_vowels
#     }

# # Example usage
# filename = "sample.txt"  # Replace with your actual file name
# stats = file_stats(filename)
# print(stats)
