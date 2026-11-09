# Question 7: Enter time in minutes and print it in hour-and-minute format.

total_minutes = int(input("Enter time in minutes: "))

if total_minutes < 0:
    print("Time in minutes cannot be negative.")
else:
    hours, minutes = divmod(total_minutes, 60)
    print(f"{hours} hour(s) and {minutes} minute(s)")