# 📘 Lecture 8 – OOP in Python (Apna College)

# ✅ 1. Basic Class and Object Example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Sachin", [85, 90, 95])
print("Student Name:", s1.name)
print("Average Marks:", s1.get_average())


# ✅ 2. Bank Account Class Example
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance is ₹{self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance is ₹{self.balance}.")
        else:
            print("Insufficient balance!")

acc1 = BankAccount("Sachin", 5000)
acc1.deposit(1500)
acc1.withdraw(2000)
acc1.withdraw(6000)


# ✅ 3. Book Class with Issue/Return
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print(f"Book '{self.title}' issued.")
        else:
            print("Book already issued.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(f"Book '{self.title}' returned.")
        else:
            print("Book was not issued.")

book1 = Book("Python Basics", "Apna College")
book1.issue_book()
book1.return_book()
book1.return_book()
