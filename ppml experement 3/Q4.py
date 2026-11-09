# Question 4: Check whether a string is symmetrical or a palindrome.

text = input("Enter a string: ")
middle = len(text) // 2

if len(text) % 2 == 0:
    first_half = text[:middle]
    second_half = text[middle:]
else:
    first_half = text[:middle]
    second_half = text[middle + 1:]

if first_half == second_half:
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")