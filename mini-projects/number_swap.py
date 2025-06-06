# Project: Number Swapper
# Description: Swaps two numbers using a third variable
# Author: Sachin Singh

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# Swapping using a third variable
temp = a
a = b
b = temp

print("✅ Numbers after swapping:")
print(f"First number: {a}")
print(f"Second number: {b}")
