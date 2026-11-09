# Question 4: Create a function that prints the first 15 Fibonacci terms
# without using recursion.

def print_fibonacci():
    first, second = 0, 1
    terms = []
    for _ in range(15):
        terms.append(first)
        first, second = second, first + second
    print("First 15 Fibonacci terms:", *terms)


print_fibonacci()