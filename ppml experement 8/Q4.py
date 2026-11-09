numbers = [
    int(value)
    for value in input("Enter integers separated by spaces: ").split()
]

if not numbers:
    print("Enter at least one integer to calculate the ratios.")
else:
    classifications = list(
        map(
            lambda number: "positive" if number > 0
            else "negative" if number < 0
            else "zero",
            numbers,
        )
    )
    total = len(numbers)

    for category in ("positive", "negative", "zero"):
        count = len(list(filter(lambda sign: sign == category, classifications)))
        percentage = count / total * 100
        print(f"{category.title()}: {count}/{total} ({percentage:.2f}%)")
