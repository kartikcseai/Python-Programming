#Write a program that accepts a sentence and calculate the number of digits, uppercase and lowercase letters.

def count_characters(sentence):
    digits = sum(c.isdigit() for c in sentence)
    uppercase = sum(c.isupper() for c in sentence)
    lowercase = sum(c.islower() for c in sentence)

    print(f"Digits: {digits}")
    print(f"Uppercase Letters: {uppercase}")
    print(f"Lowercase Letters: {lowercase}")

# Accept user input
sentence = input("Enter a sentence: ")
count_characters(sentence)
