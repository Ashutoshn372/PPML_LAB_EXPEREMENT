# Question 2: Enter the three sides of a triangle and find its area.

import math

side_a = float(input("Enter the first side: "))
side_b = float(input("Enter the second side: "))
side_c = float(input("Enter the third side: "))

if side_a <= 0 or side_b <= 0 or side_c <= 0:
    print("The sides must be positive.")
elif side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
    print("The given sides do not form a triangle.")
else:
    semi_perimeter = (side_a + side_b + side_c) / 2
    area = math.sqrt(
        semi_perimeter
        * (semi_perimeter - side_a)
        * (semi_perimeter - side_b)
        * (semi_perimeter - side_c)
    )
    print("Area of the triangle:", area)