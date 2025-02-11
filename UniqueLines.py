# Write a function that reads a file and writes the unique lines to a new file.

def write_unique_lines(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w') as outfile:
        for line in lines:
            if line not in seen_lines:
                outfile.write(line)
                seen_lines.add(line)

# Example usage
input_file = "input.txt"
output_file = "output.txt"
write_unique_lines(input_file, output_file)
print("Unique lines have been written to the output file.")
