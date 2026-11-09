try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    quotient = numerator / denominator
except ValueError:
    print("Invalid input: please enter numeric values.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Quotient:", quotient)
finally:
    print("Exception handling demonstration finished.")
