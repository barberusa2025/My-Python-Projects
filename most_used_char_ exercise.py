# This code counts the frequency of each character in a given sentence
sentence = "This is a common interview question."

char_count = {}
for char in sentence:
    if char.isalpha():  # Count only alphabetic characters
        char = char.lower()  # Normalize to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Sort the dictionary by frequency of characters
# and return the most used character
char_frequency_sorted = sorted(
    char_count.items(),
    key=lambda item: item[1],
    reverse=True)

print(char_frequency_sorted[0])  # Print the most used character and its count
