# Lecture 4: Dictionary and Set Practice

# Q1: Store word meanings in a dictionary
word_meanings = {
    "table": "a piece of furniture",
    "cat": "a small animal"
}
print("Word Meanings:", word_meanings)

# Q2: Store marks of 3 subjects from user
marks = {}
marks["Math"] = int(input("Enter marks for Math: "))
marks["Science"] = int(input("Enter marks for Science: "))
marks["English"] = int(input("Enter marks for English: "))
print("Marks Dictionary:", marks)

# Q3: Number of classrooms needed for subjects
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
unique_subjects = set(subjects)
print("Number of classrooms needed:", len(unique_subjects))

# Q4: Store 9 and 9.0 as separate values in a set
my_set = {9, "9.0"}
print("Set with separate values:", my_set)
