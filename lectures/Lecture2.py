# Lecture 2 – Strings & Conditionals (Apna College)

# 1. String Basics
str1 = "Apna"
str2 = "College"
full = str1 + str2
print("Concatenated:", full)
print("Length:", len(full))

# 2. Indexing & Slicing
str3 = "ApnaCollege"
print("Index 0:", str3[0])
print("Slicing [1:4]:", str3[1:4])
print("Negative Slicing [-3:-1]:", str3[-3:-1])

# 3. String Functions
s = "I am a coder."
print(s.endswith("er."))
print(s.count("am"))
print(s.capitalize())
print(s.find("coder"))
print(s.replace("coder", "developer"))

# 4. Practice – User input and string handling
first_name = input("Enter your first name: ")
print("Length of your name:", len(first_name))

str4 = input("Enter a string with $ sign: ")
print("Occurrences of $:", str4.count('$'))

# 5. Conditional Statements
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 6. Practice – Conditions
# Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Greatest of 3 numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

# Multiple of 7
n = int(input("Enter number: "))
if n % 7 == 0:
    print("Multiple of 7")
else:
    print("Not a multiple of 7")
