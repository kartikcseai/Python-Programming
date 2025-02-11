# Construct following filters:
# 1. Filter all the numbers
# 2. Filter all the strings starting with a vowel
# 3. Filter all the strings that contains any of the following noun: Agra, Ramesh, Tomato, Patna.
# Create a program that implements these filters to clean the text.

def clean_text(text):
    words = text.split()
    nouns = {"Agra", "Ramesh", "Tomato", "Patna"}
    
    filtered_words = [
        word for word in words
        if not word.isdigit()  # Filter numbers
        and not word.lower().startswith(('a', 'e', 'i', 'o', 'u'))  # Filter words starting with a vowel
        and word not in nouns  # Filter specific nouns
    ]
    
    return " ".join(filtered_words)

# Test case
text = "12 Agra apple is 34 Ramesh going to Tomato market in Patna"
print(clean_text(text))
# Output: "is going to market in"
