def read_integer_list(name):
    values = input(f"Enter integers for {name}, separated by spaces: ").split()
    return [int(value) for value in values]


first_list = read_integer_list("the first list")
second_list = read_integer_list("the second list")
third_list = read_integer_list("the third list")

if len(first_list) != len(second_list) or len(first_list) != len(third_list):
    print("All three lists must have the same number of elements.")
else:
    sums = list(map(lambda first, second, third: first + second + third,
                    first_list, second_list, third_list))
    print("Sum of the three lists:", sums)