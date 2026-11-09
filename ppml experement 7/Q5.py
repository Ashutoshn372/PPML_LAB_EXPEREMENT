integer_list = [
    int(value)
    for value in input("Enter integers for the list, separated by spaces: ").split()
]
integer_tuple = tuple(
    int(value)
    for value in input("Enter integers for the tuple, separated by spaces: ").split()
)

string_list = list(map(str, integer_list))
string_list_from_tuple = list(map(str, integer_tuple))

print("List converted to strings:", string_list)
print("Tuple converted to a list of strings:", string_list_from_tuple)