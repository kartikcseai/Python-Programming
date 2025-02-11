# Construct a program which accepts a sequence of words separated by whitespace as file input. Print the words composed of digits only. 

def extract_numbers(text):
    return " ".join([word for word in text.split() if word.isdigit()])

# Test case
text = "hello 123 world 456 78abc 90"
print(extract_numbers(text))
# Output: "123 456 90"


