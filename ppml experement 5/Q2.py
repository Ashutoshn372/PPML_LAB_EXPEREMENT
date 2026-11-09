count = int(input("How many key-value pairs are in the dictionary? "))
dictionary = {}

for index in range(count):
    key = input(f"Enter key {index + 1}: ")
    value = int(input(f"Enter integer value for {key}: "))
    dictionary[key] = value

if not dictionary:
    print("The dictionary is empty.")
else:
    maximum_value = max(dictionary.values())
    maximum_keys = [
        key for key, value in dictionary.items() if value == maximum_value
    ]
    print("Maximum value:", maximum_value)
    print("Key(s) with the maximum value:", maximum_keys)