# Project: Greatest Number Checker
# Description: Finds the greatest among three numbers with equality checks
# Author: Sachin Singh

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

if a > b and a > c:
    print("First number is the greatest.")
elif b > a and b > c:
    print("Second number is the greatest.")
elif c > a and c > b:
    print("Third number is the greatest.")
elif a == b > c:
    print("First and second numbers are equal and greatest.")
elif b == c > a:
    print("Second and third numbers are equal and greatest.")
elif a == c > b:
    print("First and third numbers are equal and greatest.")
else:
    print("All numbers are equal.")
