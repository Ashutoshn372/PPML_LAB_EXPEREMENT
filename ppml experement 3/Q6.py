# Question 6: Remove all duplicate characters from a string.

text = input("Enter a string: ")
unique_characters = []

for character in text:
    if character not in unique_characters:
        unique_characters.append(character)

print("String without duplicates:", "".join(unique_characters))