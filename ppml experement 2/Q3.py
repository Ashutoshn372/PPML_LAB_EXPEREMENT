# Question 3: Enter a number and check whether it is a palindrome.

number = input("Enter an integer: ").strip()

is_negative = number.startswith("-")
if number.startswith(("-", "+")):
    digits = number[1:]
else:
    digits = number

if not digits.isdigit():
    print("Please enter a valid integer.")
elif not is_negative and digits == digits[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")