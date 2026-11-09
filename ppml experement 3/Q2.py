# Question 2: Find the factorial of a number.

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(2, number + 1):
        factorial *= value
    print(f"{number}! = {factorial}")