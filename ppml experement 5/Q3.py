count = int(input("How many key-value pairs are in the dictionary? "))
dictionary = {}

for index in range(count):
    key = input(f"Enter key {index + 1}: ")
    value = input(f"Enter value for {key}: ")
    dictionary[key] = value

unique_dictionary = {}
seen_values = set()

for key, value in dictionary.items():
    if value not in seen_values:
        unique_dictionary[key] = value
        seen_values.add(value)

print("Dictionary after removing duplicate values:", unique_dictionary)