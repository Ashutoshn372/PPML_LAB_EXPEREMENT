# Question 1: Enter two integers and perform all arithmetic operations on them.

first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Exponentiation:", first_number ** second_number)

if second_number == 0:
    print("Division, floor division, and modulo are undefined when the second integer is zero.")
else:
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Modulo:", first_number % second_number)