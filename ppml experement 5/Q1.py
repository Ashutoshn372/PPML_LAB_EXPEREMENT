def read_dictionary(name):
    count = int(input(f"How many key-value pairs are in {name}? "))
    dictionary = {}

    for index in range(count):
        key = input(f"Enter key {index + 1}: ")
        value = input(f"Enter value for {key}: ")
        dictionary[key] = value

    return dictionary


first_dictionary = read_dictionary("the first dictionary")
second_dictionary = read_dictionary("the second dictionary")

merged_dictionary = first_dictionary.copy()
merged_dictionary.update(second_dictionary)

print("Merged dictionary:", merged_dictionary)