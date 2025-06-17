# Lecture 7 – File Handling in Python
# Author: Sachin Singh

# 1. Writing to a File
with open("data.txt", "w") as file:
    file.write("Hello, this is Sachin!\n")
    file.write("I'm learning File Handling in Python.\n")

# 2. Reading from the File
with open("data.txt", "r") as file:
    content = file.read()
    print("📖 File Content:\n", content)

# 3. Appending to the File
with open("data.txt", "a") as file:
    file.write("This line is added using append mode.\n")

# 4. Reading Again to Show Update
with open("data.txt", "r") as file:
    print("\n📖 Updated File Content:\n", file.read())

# 5. Writing List of Lines Using writelines()
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("lines.txt", "w") as file:
    file.writelines(lines)

# 6. Mini Project: Notes Writer App
def write_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

write_note("✅ This is my first note.")
write_note("🚀 File handling is fun!")

# Done ✅
