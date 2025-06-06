# Project: Simple Interest Calculator
# Description: Calculates simple interest based on user input
# Author: Sachin Singh

principal = int(input("Enter principal amount: ₹"))
rate = int(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print(f"📈 Your interest is: ₹{simple_interest}")
