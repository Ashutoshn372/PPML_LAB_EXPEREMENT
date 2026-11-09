# Question 2: Enter a 5-digit number and print the digits at odd locations.

number = input("Enter a 5-digit number: ").strip()

if len(number) != 5 or not number.isdigit():
    print("Please enter exactly five digits.")
else:
    odd_location_digits = number[::2]
    print("Digits at odd locations (1, 3, 5):", " ".join(odd_location_digits))