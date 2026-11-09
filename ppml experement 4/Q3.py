# Question 3: Create a list of 20 integers and increase each odd value by 5.

numbers = []
for index in range(20):
    numbers.append(int(input(f"Enter integer {index + 1}: ")))

for index in range(len(numbers)):
    if numbers[index] % 2 != 0:
        numbers[index] += 5

print("Updated list:", numbers)