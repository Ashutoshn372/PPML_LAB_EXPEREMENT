first_set = set(input("Enter the first group of strings separated by spaces: ").split())
second_set = set(input("Enter the second group of strings separated by spaces: ").split())

combined_set = first_set | second_set

print("Combined set without duplicates:", combined_set)