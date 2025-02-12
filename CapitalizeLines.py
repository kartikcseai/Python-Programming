#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#e.g. If Input:
#Hello world
#Practice makes perfect
#Then, Output:
#HELLO WORLD
#PRACTICE MAKES PERFECT

def capitalize_lines():
    print("Enter multiple lines (press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":  # Stop input when an empty line is entered
            break
        lines.append(line.upper())  # Convert line to uppercase and store it
    
    print("\nCapitalized Output:")
    for line in lines:
        print(line)  # Print each capitalized line

# Run the function
capitalize_lines()
