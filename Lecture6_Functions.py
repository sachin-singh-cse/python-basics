# Lecture 6 – Functions in Python
# Author: Sachin Singh

# 1. Creating a Simple Function
def greet():
    print("Hello from Sachin!")

greet()

# 2. Function with Parameters
def greet_user(name):
    print("Hello", name)

greet_user("Sachin")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)

# 4. Default Parameters
def power(a, b=2):
    return a ** b

print("Power:", power(5))
print("Power with both args:", power(2, 3))

# 5. Function to Print List Elements
def print_list(lst):
    for item in lst:
        print(item, end=" ")
    print()

print_list([10, 20, 30])

# 6. Function to Find Factorial using Loop
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))

# 7. Recursive Function (Sum of first n natural numbers)
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print("Recursive Sum:", recursive_sum(5))

# 8. Recursive Factorial Function
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

print("Recursive Factorial:", recursive_factorial(4))
