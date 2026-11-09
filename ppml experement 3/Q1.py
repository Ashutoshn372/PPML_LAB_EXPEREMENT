# Question 1: Print twin prime numbers between 1 and N.

limit = int(input("Enter N: "))

if limit < 1:
    print("N must be at least 1.")
else:
    print(f"Twin prime pairs between 1 and {limit}:")
    for first in range(2, limit - 1):
        second = first + 2
        first_is_prime = all(first % divisor != 0 for divisor in range(2, int(first**0.5) + 1))
        second_is_prime = all(second % divisor != 0 for divisor in range(2, int(second**0.5) + 1))
        if first_is_prime and second_is_prime:
            print(first, "and", second)