def capitalize_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = content.title()
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Example usage
file_path = "example.txt"
capitalize_file_content(file_path)
print("File content modified successfully.")
