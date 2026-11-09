values = input("Enter set elements separated by spaces: ").split()
original_set = set(values)
copied_set = set()

for element in original_set:
    copied_set.add(element)

print("Original set:", original_set)
print("Copied set:", copied_set)