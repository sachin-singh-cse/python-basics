# Lecture 4 – Dictionary and Set in Python

# 1. Dictionary Basics
word_meanings = {
    "table": "a piece of furniture",
    "cat": "a small animal"
}
print("Word Meanings:", word_meanings)

# 2. Add subject marks into a dictionary
marks = {}
marks["Math"] = int(input("Enter marks for Math: "))
marks["Science"] = int(input("Enter marks for Science: "))
marks["English"] = int(input("Enter marks for English: "))
print("Marks Dictionary:", marks)

# 3. Dictionary methods
myDict = {
    "name": "Sachin",
    "cgpa": 8.5,
    "marks": [87, 92, 75]
}
print("Keys:", myDict.keys())
print("Values:", myDict.values())
print("Items:", myDict.items())
print("Get CGPA:", myDict.get("cgpa"))

# 4. Nested Dictionary Example
student = {
    "name": "Amit",
    "score": {
        "math": 90,
        "science": 95
    }
}
print("Math Score:", student["score"]["math"])

# 5. Set Basics
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
unique_subjects = set(subjects)
print("Unique Subjects:", unique_subjects)
print("Number of classrooms needed:", len(unique_subjects))

# 6. Separate 9 and 9.0 using set
my_set = {9, "9.0"}
print("Set with separate 9 and 9.0:", my_set)

# 7. Set Methods
mySet = {1, 2, 3}
mySet.add(4)
mySet.remove(2)
print("Modified Set:", mySet)
