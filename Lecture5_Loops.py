# Lecture 5 – Loops in Python

# 1. Print numbers from 1 to 100 using for loop
for i in range(1, 101):
    print(i, end=" ")
print()

# 2. Print numbers from 100 to 1 using for loop
for i in range(100, 0, -1):
    print(i, end=" ")
print()

# 3. Print square numbers using loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in nums:
    print(num, end=" ")
print()

# 4. Multiplication table of a number n
n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# 5. Search for number x in the list
x = int(input("Enter number to search: "))
found = False
for num in nums:
    if num == x:
        found = True
        break
if found:
    print(f"{x} found in list.")
else:
    print(f"{x} not found.")

# 6. While loop example – Print 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# 7. Break & Continue Example – Skip multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# 8. pass Statement Example
for i in range(5):
    pass
