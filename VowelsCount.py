#Write a python program to count the vowels present in given input string. Explain the output of program through example.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Defining vowels (both lowercase and uppercase)
    count = 0  # Initializing vowel count to zero
    
    for char in input_string:
        if char in vowels:
            count += 1  # Increment count if character is a vowel
    
    return count

# Example usage:
input_string = input("Enter a string: ")  # Taking user input
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the given string: {vowel_count}")
