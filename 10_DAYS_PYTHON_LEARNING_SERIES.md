# 🐍 10 Days Python Learning Series: Beginner to Advanced

A comprehensive learning roadmap to master Python from zero to hero in 10 days!

---

## 📋 Course Overview

This series is designed to take you through Python fundamentals, intermediate concepts, and advanced topics. Each day builds upon the previous one with practical exercises and real-world examples.

---

## 🗓️ Day-by-Day Breakdown

### **Day 1: Python Basics & Environment Setup**
**Duration:** 2-3 hours

**Topics:**
- Introduction to Python and why Python?
- Installing Python and setting up development environment
- Understanding Python IDE/Editors (VS Code, PyCharm, Jupyter)
- Running your first Python program
- Python syntax basics
- Comments, variables, and data types (int, float, string, bool)

**Hands-on Exercise:**
```python
# Exercise: Create variables and print them
name = "Python Learner"
age = 25
gpa = 3.8
is_student = True

print(f"Name: {name}, Age: {age}, GPA: {gpa}, Student: {is_student}")
```

**Resources:**
- Python Official Documentation: https://docs.python.org/3/
- Interactive Python Tutorial: https://www.python.org/about/gettingstarted/

---

### **Day 2: Data Types & Operations**
**Duration:** 2-3 hours

**Topics:**
- Strings: creation, slicing, methods (upper, lower, replace, split, join)
- Numbers: arithmetic operations, type conversion
- Lists: creation, indexing, slicing, methods (append, extend, insert, remove, pop)
- Tuples: immutability, unpacking
- Dictionaries: key-value pairs, methods (get, keys, values, items)
- Type checking with isinstance()

**Hands-on Exercise:**
```python
# Exercise: Working with data structures
fruits = ["apple", "banana", "cherry"]
person = {"name": "John", "age": 30, "city": "NYC"}
coordinates = (10, 20, 30)

# List operations
fruits.append("date")
print(fruits)

# Dictionary operations
print(person["name"])
print(person.get("age"))

# Tuple unpacking
x, y, z = coordinates
print(f"Coordinates: {x}, {y}, {z}")
```

**Resources:**
- Python Data Types Guide: https://docs.python.org/3/tutorial/datastructures.html

---

### **Day 3: Control Flow & Conditionals**
**Duration:** 2-3 hours

**Topics:**
- If, elif, else statements
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Ternary operators
- Switch-like patterns (if-elif-else chains)

**Hands-on Exercise:**
```python
# Exercise: Grade calculator
marks = 85

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Marks: {marks}, Grade: {grade}")

# Ternary operator
status = "Pass" if marks >= 60 else "Fail"
print(status)
```

**Resources:**
- Control Flow Tutorial: https://docs.python.org/3/tutorial/controlflow.html

---

### **Day 4: Loops & Iterations**
**Duration:** 2-3 hours

**Topics:**
- For loops: range(), enumerate(), zip()
- While loops: conditions and break/continue
- Nested loops
- Loop control statements (break, continue, pass)
- List comprehensions
- Dictionary & set comprehensions

**Hands-on Exercise:**
```python
# Exercise: Loop demonstrations
# For loop with range
for i in range(1, 6):
    print(f"Number: {i}")

# Enumerate for index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

**Resources:**
- Loops in Python: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements

---

### **Day 5: Functions & Scope**
**Duration:** 2-3 hours

**Topics:**
- Defining functions with def
- Parameters and arguments (positional, keyword, default, *args, **kwargs)
- Return values and multiple returns
- Scope: local, global, nonlocal
- Lambda functions (anonymous functions)
- Docstrings and type hints
- Decorators basics

**Hands-on Exercise:**
```python
# Exercise: Function demonstrations
def greet(name, greeting="Hello"):
    """Greet someone with a custom greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# Functions with multiple arguments
def add(a, b):
    return a + b

# Lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Function with *args and **kwargs
def print_info(*args, **kwargs):
    for arg in args:
        print(f"Arg: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(1, 2, 3, name="John", age=30)
```

**Resources:**
- Functions in Python: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

---

### **Day 6: Object-Oriented Programming (OOP) Basics**
**Duration:** 2-3 hours

**Topics:**
- Classes and objects
- Attributes and methods
- Constructors (__init__)
- Instance and class variables
- Special methods (__str__, __repr__, __len__)
- Inheritance: single and multiple
- Method overriding
- super() function

**Hands-on Exercise:**
```python
# Exercise: Simple OOP example
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

# Create instances
dog = Dog("Buddy", "Dog")
print(dog)
print(dog.speak())
```

**Resources:**
- OOP in Python: https://docs.python.org/3/tutorial/classes.html

---

### **Day 7: Advanced OOP & File Handling**
**Duration:** 2-3 hours

**Topics:**
- Encapsulation: private/protected attributes (_var, __var)
- Properties and getters/setters (@property)
- Polymorphism
- Abstract base classes (ABC)
- File I/O: open, read, write, close
- Context managers (with statement)
- Reading/writing JSON, CSV files
- Exception handling in file operations

**Hands-on Exercise:**
```python
# Exercise: File handling
# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python is awesome!")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Working with JSON
import json

data = {"name": "John", "age": 30, "city": "NYC"}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

**Resources:**
- File I/O in Python: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

### **Day 8: Error Handling & Debugging**
**Duration:** 2-3 hours

**Topics:**
- Exception types (ValueError, TypeError, KeyError, IndexError, etc.)
- Try-except-else-finally blocks
- Raising custom exceptions
- Exception chaining
- Logging module for debugging
- Debugging techniques: print statements, debugger, pdb
- Common errors and best practices

**Hands-on Exercise:**
```python
# Exercise: Exception handling
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete!")

# Custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught custom error: {e}")
```

**Resources:**
- Exception Handling: https://docs.python.org/3/tutorial/errors.html

---

### **Day 9: Working with Libraries & Modules**
**Duration:** 2-3 hours

**Topics:**
- Importing modules (import, from...import, as)
- Standard library modules: os, sys, datetime, random, math, collections
- Third-party libraries: requests, numpy, pandas
- Installing packages with pip
- Virtual environments (venv)
- Creating your own modules
- Package structure

**Hands-on Exercise:**
```python
# Exercise: Working with libraries
import datetime
import random
import math
from collections import Counter

# datetime
now = datetime.datetime.now()
print(f"Current time: {now}")

# random
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# math
pi = math.pi
print(f"Pi: {pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# collections
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(numbers)
print(f"Most common: {counter.most_common(1)}")

# requests (third-party, requires: pip install requests)
# import requests
# response = requests.get("https://api.github.com")
# print(response.json())
```

**Resources:**
- Python Standard Library: https://docs.python.org/3/library/
- PyPI (Python Package Index): https://pypi.org/

---

### **Day 10: Projects & Advanced Topics**
**Duration:** 3-4 hours

**Topics:**
- Building a complete project
- Integrating multiple concepts
- Best practices: PEP 8, naming conventions, code organization
- Testing: unittest, pytest
- Code quality tools: linters (pylint, flake8), formatters (black)
- Performance optimization: timing, profiling
- Introduction to frameworks: Flask, Django
- Real-world applications and next steps

**Sample Project: Todo Application**

```python
# todo_app.py
import json
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task):
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task}")
    
    def list_todos(self):
        if not self.todos:
            print("No todos!")
            return
        for todo in self.todos:
            status = "✓" if todo["completed"] else "○"
            print(f"{status} {todo['id']}. {todo['task']}")
    
    def complete_todo(self, todo_id):
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.save_todos()
                print(f"✓ Completed: {todo['task']}")
                return
        print("Todo not found!")
    
    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo["id"] != todo_id]
        self.save_todos()
        print(f"✓ Deleted todo {todo_id}")

# Main program
if __name__ == "__main__":
    app = TodoApp()
    
    while True:
        print("\n--- Todo App ---")
        print("1. Add todo")
        print("2. List todos")
        print("3. Complete todo")
        print("4. Delete todo")
        print("5. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                app.add_todo(task)
        elif choice == "2":
            app.list_todos()
        elif choice == "3":
            try:
                todo_id = int(input("Enter todo ID: "))
                app.complete_todo(todo_id)
            except ValueError:
                print("Invalid ID!")
        elif choice == "4":
            try:
                todo_id = int(input("Enter todo ID: "))
                app.delete_todo(todo_id)
            except ValueError:
                print("Invalid ID!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
```

**Resources:**
- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/
- Flask Framework: https://flask.palletsprojects.com/
- Django Framework: https://www.djangoproject.com/

---

## 📚 Additional Learning Resources

### Documentation & Tutorials
- **Official Python Docs:** https://docs.python.org/3/
- **Real Python:** https://realpython.com/
- **GeeksforGeeks Python:** https://www.geeksforgeeks.org/python-programming-language/
- **Codecademy:** https://www.codecademy.com/learn/learn-python-3

### Practice Platforms
- **LeetCode:** https://leetcode.com/ (Algorithm practice)
- **HackerRank:** https://www.hackerrank.com/domains/python
- **Codewars:** https://www.codewars.com/
- **Project Euler:** https://projecteuler.net/

### YouTube Channels
- **Corey Schafer:** Python tutorials and best practices
- **Tech With Tim:** Python projects and tutorials
- **Programming with Mosh:** Beginner-friendly Python courses

---

## 💡 Tips for Success

1. **Code Along:** Don't just read, type every example yourself
2. **Experiment:** Modify examples and see what happens
3. **Build Projects:** Apply what you learn to real problems
4. **Debug Actively:** Learn to use debugging tools
5. **Read Others' Code:** Study how experienced developers write Python
6. **Practice Regularly:** Consistency beats intensity
7. **Join Communities:** Python community is very welcoming (Reddit, Discord, Stack Overflow)
8. **Build Something You Care About:** Motivation comes from personal interest

---

## 🎯 Next Steps After Day 10

- **Web Development:** Learn Flask or Django
- **Data Science:** Explore NumPy, Pandas, Matplotlib, Scikit-learn
- **Machine Learning:** TensorFlow, PyTorch, Keras
- **Automation:** Selenium, Beautiful Soup for web scraping
- **Contribute to Open Source:** Start contributing to Python projects on GitHub
- **Specialize:** Choose an area that interests you most

---

## 📞 Get Help

- **Stack Overflow:** https://stackoverflow.com/questions/tagged/python
- **Python Discord Communities:** Look for Python learning servers
- **GitHub Issues:** Ask questions in relevant repositories
- **Reddit:** r/learnprogramming, r/Python

---

**Happy Learning! 🚀 Start your Python journey today and become a Python Hero!**

*Last Updated: May 2026*
