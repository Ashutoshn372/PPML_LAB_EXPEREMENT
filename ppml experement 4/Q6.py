# Question 6: Calculate the factorial of a number using recursion.

def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number < 2:
        return 1
    return number * factorial(number - 1)


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"{number}! = {factorial(number)}")