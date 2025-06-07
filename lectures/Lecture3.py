# Lecture 3 – Lists and Tuples in Python (Apna College)

# 1. Creating Lists
marks = [87, 64, 33, 95, 76]
student = ["Karan", 85, "Delhi"]
print("Marks:", marks)
print("Student:", student)

# 2. List Indexing & Slicing
print("marks[1:4]:", marks[1:4])
print("marks[:4]:", marks[:4])
print("marks[1:]:", marks[1:])
print("marks[-3:-1]:", marks[-3:-1])

# 3. List Methods
numbers = [2, 1, 3]
numbers.append(4)
numbers.insert(1, 10)
numbers.sort()
numbers.reverse()
numbers.sort(reverse=True)
print("Modified List:", numbers)

# 4. Removing elements
numbers.remove(10)  # Removes first occurrence of 10
numbers.pop(2)      # Removes element at index 2
print("After Removal:", numbers)

# 5. Tuples
tup = (87, 64, 33, 95, 76)
print("Tuple:", tup)

# tup[0] = 43  # Not allowed (Immutable)

# Tuple methods
tup2 = (2, 1, 3, 1)
print("Index of 1:", tup2.index(1))
print("Count of 1:", tup2.count(1))

# 6. Practice Questions

# Q1. Take 3 movie names from user
movies = []
for i in range(3):
    name = input(f"Enter movie {i+1}: ")
    movies.append(name)
print("Favorite Movies:", movies)

# Q2. Check if a list is palindrome
palin = [1, 2, 3, 2, 1]
if palin == palin[::-1]:
    print("Palindrome List")
else:
    print("Not a Palindrome")

# Q3. Count number of A grade students
grades = ("C", "D", "A", "A", "B", "B", "A")
print("A Grade Count:", grades.count("A"))

# Q4. Sort the grades from A to D
grade_list = list(grades)
grade_list.sort()
print("Sorted Grades:", grade_list)
