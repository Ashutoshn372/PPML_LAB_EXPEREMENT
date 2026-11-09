# Question 1: Enter a percentage and display its grade.

percentage = float(input("Enter a percentage (0-100): "))

if not 0 <= percentage <= 100:
    print("Percentage must be between 0 and 100.")
elif percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")