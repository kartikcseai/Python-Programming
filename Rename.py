# write a python program to rename a fileimport os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
old_filename = "old_file.txt"
new_filename = "new_file.txt"
rename_file(old_filename, new_filename)
  
 