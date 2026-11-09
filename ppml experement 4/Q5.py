# Question 5: Create a function that returns the even values in a list.

def get_even_values(values):
    return [value for value in values if value % 2 == 0]


numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
print("Even values:", get_even_values(numbers))