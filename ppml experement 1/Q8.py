# Question 8: Enter two integers and swap them using bitwise operators.

first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))

first_number = first_number ^ second_number
second_number = first_number ^ second_number
first_number = first_number ^ second_number

print("After swapping:")
print("First integer:", first_number)
print("Second integer:", second_number)