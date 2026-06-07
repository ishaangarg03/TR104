# =============================================================================
# WEEK 2 - DAY 3: Object-Oriented Programming (OOP)
# Topic: Classes, Objects, Inheritance — the backbone of real-world Python
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: WHY OOP?
# So far we've written code as a sequence of instructions (procedural).
# OOP organizes code into "objects" — like real-world entities.
# Example: A "Student" has attributes (name, age) and actions (study, submit).
# -----------------------------------------------------------------------------

print("=" * 50)
print("SECTION 1: CLASSES AND OBJECTS")
print("=" * 50)

# Define a class — it's a blueprint
class Student:
    """Represents a student at an internship."""

    # __init__ is the constructor — runs when you create a new Student
    def __init__(self, name, age, department):
        # self refers to THIS specific object
        self.name = name
        self.department = department
        self.age = age
        self.skills = []           # every student starts with empty skills list

    # A method — a function that belongs to the class
    def introduce(self):
        print(f"Hi! I'm {self.name}, {self.age} years old, from {self.department}.")

    def learn_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} just learned: {skill}")

    def show_skills(self):
        if self.skills:
            print(f"{self.name}'s skills: {', '.join(self.skills)}")
        else:
            print(f"{self.name} has no skills yet.")

    # __str__ — defines what prints when you do print(student)
    def __str__(self):
        return f"Student({self.name}, {self.department})"


# Creating objects (instances) from the class
navkiran = Student("Ishaan Garg", 21, "AI & ML")
alice = Student("Alice", 22, "Web Development")

# Calling methods
navkiran.introduce()
alice.introduce()

navkiran.learn_skill("Python")
navkiran.learn_skill("Git")
navkiran.learn_skill("APIs")
navkiran.show_skills()

alice.learn_skill("HTML")
alice.learn_skill("CSS")
alice.show_skills()

print("\nPrinting object:", navkiran)   # uses __str__

# Accessing attributes directly
print(f"\n{navkiran.name} is {navkiran.age} years old.")

# -----------------------------------------------------------------------------
# SECTION 2: CLASS VARIABLES vs INSTANCE VARIABLES
# Instance variable → unique to each object (e.g., name)
# Class variable → shared across ALL objects of the class
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 2: CLASS vs INSTANCE VARIABLES")
print("=" * 50)

class Intern:
    company = "TechCorp AI"       # class variable — same for all interns
    total_interns = 0             # tracks how many interns were created

    def __init__(self, name, role):
        self.name = name          # instance variable — unique per intern
        self.role = role
        Intern.total_interns += 1  # update class variable when new intern created

    def info(self):
        print(f"{self.name} | Role: {self.role} | Company: {Intern.company}")


intern1 = Intern("Navkiran", "AI Intern")
intern2 = Intern("Priya", "Data Intern")
intern3 = Intern("Rahul", "Backend Intern")

intern1.info()
intern2.info()
intern3.info()

print(f"\nTotal interns at {Intern.company}: {Intern.total_interns}")

# -----------------------------------------------------------------------------
# SECTION 3: INHERITANCE
# A child class inherits everything from a parent class.
# This avoids repeating code — very important in large projects.
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 3: INHERITANCE")
print("=" * 50)

# Parent class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")

    def breathe(self):
        print(f"{self.name} breathes air.")

# Child class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # calls Animal's __init__
        self.breed = breed

    # Overriding a method
    def speak(self):
        print(f"{self.name} the {self.breed} barks: Woof woof!")

    def fetch(self):
        print(f"{self.name} fetches the ball! 🐕")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def speak(self):
        print(f"{self.name} says softly: Meow~")

    def purr(self):
        print(f"{self.name} purrs... 😸")


dog = Dog("Bruno", "Labrador")
cat = Cat("Whiskers")

dog.speak()
dog.breathe()     # inherited from Animal
dog.fetch()

cat.speak()
cat.breathe()     # inherited from Animal
cat.purr()

# isinstance() — check if object belongs to a class
print(f"\nIs dog an Animal? {isinstance(dog, Animal)}")
print(f"Is cat a Dog? {isinstance(cat, Dog)}")

# -----------------------------------------------------------------------------
# SECTION 4: ENCAPSULATION — PROTECTING DATA
# Use _ or __ to make attributes private (not directly accessible outside).
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 4: ENCAPSULATION")
print("=" * 50)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # __ makes it "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance         # access private data through a method


account = BankAccount("Navkiran", 5000)
account.deposit(1500)
account.withdraw(2000)
account.withdraw(9999)                # should fail

print(f"\nFinal balance: ₹{account.get_balance()}")

# This would cause an AttributeError — you can't directly access __balance
# print(account.__balance)   ← DO NOT DO THIS

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("class MyClass:       → defines a blueprint")
print("__init__(self, ...)  → constructor, runs on object creation")
print("self                 → refers to the current object")
print("Inheritance          → child class gets parent's methods")
print("super().__init__()   → calls parent constructor")
print("self.__attr          → private attribute (encapsulated)")
print("isinstance(obj, Cls) → checks if object is of a class")
