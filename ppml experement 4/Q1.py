# Question 1: Find the second largest and second smallest distinct values
# in a list of 10 integers without using the sort function.

numbers = []
for index in range(10):
    numbers.append(int(input(f"Enter integer {index + 1}: ")))

distinct_numbers = set(numbers)
if len(distinct_numbers) < 2:
    print("At least two distinct values are needed.")
else:
    smallest = min(distinct_numbers)
    largest = max(distinct_numbers)
    second_smallest = min(value for value in distinct_numbers if value != smallest)
    second_largest = max(value for value in distinct_numbers if value != largest)
    print("Second smallest:", second_smallest)
    print("Second largest:", second_largest)