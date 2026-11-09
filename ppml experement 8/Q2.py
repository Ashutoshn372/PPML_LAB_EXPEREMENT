numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
tripled_numbers = list(map(lambda number: number * 3, numbers))

print("Tripled numbers:", tripled_numbers)
