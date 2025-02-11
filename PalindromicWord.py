# Description: This program reads a list of words from a file and writes the palindromes to another file.
# example : innput file contains "Level up your programming skills. Madam and eve are famous."
# output file should contain "['level', 'madam', 'eve']"

def find_palindromes(input_file, output_file):
    with open(input_file, 'r') as infile:
        words = infile.read().split()
    
    palindromes = [word for word in words if word == word[::-1]]
    
    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(palindromes))

# Example usage
input_file = "input.txt"
output_file = "palindromes.txt"
find_palindromes(input_file, output_file)
print("Palindromes have been written to the output file.")