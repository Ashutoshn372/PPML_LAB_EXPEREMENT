# Question 2: Create a list of 5 integers and a list of 5 strings, then
# print one element from each list combined at a time.

integers = []
for index in range(5):
    integers.append(int(input(f"Enter integer {index + 1}: ")))

words = []
for index in range(5):
    words.append(input(f"Enter string {index + 1}: "))

print("Combined elements:")
for integer, word in zip(integers, words):
    print(integer, word)