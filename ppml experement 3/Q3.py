# Question 3: Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year <= 0:
    print("Please enter a positive year.")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")