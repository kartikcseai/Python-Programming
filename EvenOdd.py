# There is a file named Input.Txt. Enter some positive numbers into the file named Input.Txt. Read the contents of the file and if it is an odd number write it to ODD.TXT and if the number is even, write it to EVEN.TXT. If the file does not exist, print a message to the screen.

# Function to process numbers and categorize them as even or odd
def process_numbers():
    try:
        # Open the input file and read numbers
        with open("Input.Txt", "r") as infile:
            numbers = infile.readlines()
        
        # Open output files for even and odd numbers
        with open("EVEN.TXT", "w") as even_file, open("ODD.TXT", "w") as odd_file:
            for num in numbers:
                num = num.strip()
                if num.isdigit():  # Ensure the input is a positive number
                    num = int(num)
                    if num % 2 == 0:
                        even_file.write(f"{num}\n")
                    else:
                        odd_file.write(f"{num}\n")
        
        print("Processing complete. Check EVEN.TXT and ODD.TXT for results.")

    except FileNotFoundError:
        print("Input.Txt not found. Please create the file and add numbers.")

# Writing sample data to Input.Txt for testing
with open("Input.Txt", "w") as f:
    f.write("12\n3\n45\n8\n21\n30\n")

# Run the function
process_numbers()
