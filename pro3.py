# ------------------ EASY LEVEL ------------------

# Test case 1 : Even or Odd (Nomor 1)
def check_even_odd(num): return "The number is Even" if num % 2 == 0 else "The number is Odd"

# Test case 2 : Positive, Negative, or Zero (Nomor 2)
def check_number(num): return "The number is Positive" if num > 0 else ("The number is Negative" if num < 0 else "The number is Zero")


# ------------------ MEDIUM LEVEL ------------------

# Test case 3 : Anagram check (Nomor 3)
def is_anagram(str1, str2): return sorted(str1) == sorted(str2)

# Test case 4 : Factorial (Nomor 4)
def factorial(n): return 1 if n == 0 else n * factorial(n - 1)


# ------------------ HARD LEVEL ------------------

# Test case 5 : Palindrome (Nomor 5)
def is_palindrome(s): return s == s[::-1]

# Test case 6 : Armstrong number (Nomor 6)
def is_armstrong(num): return num == sum(int(d)**len(str(num)) for d in str(num))


# ------------------ EXPERT LEVEL ------------------

# Test case 7 : Bank Account class (Nomor 7)
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"


# Test case 8 : Student class (Nomor 8)
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."

    def get_average(self):
        return f"Average grade: {sum(self.grades)/len(self.grades):.1f}" if self.grades else "No grades available."


# ------------------ MAIN PROGRAM: RUN ALL TESTS ------------------

def separator(num):
    print("="*40)
    print(f" Hasil Output Nomor {num} ")
    print("="*40)

# Nomor 1
separator(1)
print(check_even_odd(4))
print(check_even_odd(7))

# Nomor 2
separator(2)
print(check_number(10))
print(check_number(-5))
print(check_number(0))

# Nomor 3
separator(3)
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

# Nomor 4
separator(4)
print(factorial(5))
print(factorial(0))

# Nomor 5
separator(5)
print(is_palindrome("racecar"))
print(is_palindrome("python"))
print(is_palindrome("habibah"))

# Nomor 6
separator(6)
print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(123))

# Nomor 7
separator(7)
account = BankAccount("Name")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.withdraw(600))

# Nomor 8
separator(8)
student = Student("Alice")
print(student.add_grade(90))
print(student.add_grade(80))
print(student.add_grade(70))
print(student.get_average())
