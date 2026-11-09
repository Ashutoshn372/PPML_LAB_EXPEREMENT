# Question 4: Enter the coefficients of a quadratic equation and find its roots.

import cmath

coefficient_a = float(input("Enter coefficient a: "))
coefficient_b = float(input("Enter coefficient b: "))
coefficient_c = float(input("Enter coefficient c: "))

if coefficient_a == 0:
    if coefficient_b == 0:
        if coefficient_c == 0:
            print("There are infinitely many solutions.")
        else:
            print("There is no solution.")
    else:
        root = -coefficient_c / coefficient_b
        print("This is a linear equation. Its root is:", root)
else:
    discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
    root_one = (-coefficient_b + cmath.sqrt(discriminant)) / (2 * coefficient_a)
    root_two = (-coefficient_b - cmath.sqrt(discriminant)) / (2 * coefficient_a)
    print("First root:", root_one)
    print("Second root:", root_two)