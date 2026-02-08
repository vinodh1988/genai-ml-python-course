# Python Operators: Tabulated Notes

| Operator Type      | Operators                | Description / Example                |
|--------------------|-------------------------|--------------------------------------|
| Arithmetic         | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Exponentiation |
| Assignment         | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` | Assign and update values             |
| Comparison         | `==`, `!=`, `>`, `<`, `>=`, `<=` | Compare values, returns `True`/`False` |
| Logical            | `and`, `or`, `not`      | Logical AND, OR, NOT                 |
| Bitwise            | `&`, `|`, `^`, `~`, `<<`, `>>` | Bitwise operations                   |
| Membership         | `in`, `not in`          | Test membership in sequences         |
| Identity           | `is`, `is not`          | Test object identity                 |

**Example:**
```python
a, b = 5, 2
print(a + b)      # 7 (Addition)
print(a > b)      # True (Comparison)
print(a & b)      # 0 (Bitwise AND)
print(a is b)     # False (Identity)
```

### Notes on `is` and `is not` Operators

- `is` checks if two variables point to the same object in memory.
- `is not` checks if two variables do **not** point to the same object.

**Examples:**
```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)      # False (different objects with same content)
print(x is z)      # True (same object)
print(x is not y)  # True
```

### Common Operators in Other Languages Not Present in Python

| Operator         | Languages (Examples) | Description / Usage                |
|------------------|---------------------|------------------------------------|
| `++`, `--`       | C, C++, Java        | Increment / Decrement operators    |
| `?:` (Ternary)   | C, Java, JavaScript | Ternary conditional operator       |
| `->`             | C, C++              | Pointer/member access              |
| `&` (Address-of) | C, C++              | Address-of operator                |
| `::`             | C++, Java           | Scope resolution / static access   |
| `===`, `!==`     | JavaScript, PHP     | Strict equality/inequality         |
| `>>>`            | Java, JavaScript    | Unsigned right shift               |

> Python does not support these operators directly; it uses alternative syntax or built-in functions.

## Conditional Statements in Python

Conditional statements allow you to execute code blocks based on certain conditions.

**Syntax:**
```python
if condition:
    # code block
elif another_condition:
    # another code block
else:
    # fallback code block
```

**Example:**
```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

- You can nest `if` statements.
- Conditions use comparison and logical operators.
- Indentation is required to define code blocks.
- Python supports one-line conditionals:  
  ```python
  print("Even") if x % 2 == 0 else print("Odd")
  ```
## Switch/Case Statements in Python

Python does not have a built-in `switch` or `case` statement like some other languages (e.g., C, Java, JavaScript). Instead, you can use `if-elif-else` chains or dictionary-based approaches to achieve similar functionality.

**Using `if-elif-else`:**
```python
value = 2

if value == 1:
    print("One")
elif value == 2:
    print("Two")
elif value == 3:
    print("Three")
else:
    print("Other")
```

**Using a Dictionary as a Switch:**
```python
def switch_case(value):
    return {
        1: "One",
        2: "Two",
        3: "Three"
    }.get(value, "Other")

print(switch_case(2))  # Output: Two
```

**Python 3.10+: Structural Pattern Matching (`match`):**
```python
value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")
```
- Requires Python 3.10 or newer.
- `case _:` acts as the default case.
- Useful for matching complex patterns, not just values.


## Loop Structures in Python

Loops are used to execute a block of code repeatedly.

### `for` Loop

Iterates over a sequence (like list, tuple, string, or range):

```python
for i in range(5):
    print(i)  # Prints 0 to 4

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### `while` Loop

Repeats as long as a condition is `True`:

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### Loop Control Statements

- `break`: Exit the loop immediately.
- `continue`: Skip the rest of the current iteration.
- `else`: Optional; runs if the loop wasn't terminated by `break`.

**Example:**
```python
for n in range(5):
    if n == 3:
        break
    print(n)
else:
    print("Completed without break")  # Not printed if break occurs
```

- Loops can be nested.
- Indentation defines the loop body.
- Useful for iterating, searching, and processing data.

## Jump Statements in Python

Jump statements alter the normal flow of control in loops and other code blocks.

### `break`

- Exits the nearest enclosing loop immediately.

```python
for i in range(5):
    if i == 3:
        break
    print(i)  # Prints 0, 1, 2
```

### `continue`

- Skips the rest of the current loop iteration and moves to the next iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4
```

### `pass`

- Does nothing; acts as a placeholder where code is syntactically required.

```python
for i in range(3):
    pass  # No action taken
```

### `goto`

- Python does **not** support a `goto` statement.
- Use structured control flow (`if`, `for`, `while`, functions) instead.

> Using `break` and `continue` helps manage loop execution without the need for `goto`.

## Python Modules and User-Defined Module Creation

### What is a Module?

A module is a file containing Python code (functions, classes, variables). Modules help organize code into reusable components.

**Types of Modules:**
- Built-in modules: `os`, `sys`, `math`, `json`, etc.
- User-defined modules: Custom `.py` files you create.
- Packages: Directories containing modules and an `__init__.py` file.

### Creating a User-Defined Module

Create a `.py` file with your code:

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```

Import and use it:

```python
import mymodule
print(mymodule.greet("Alice"))  # Hello, Alice!
print(mymodule.PI)              # 3.14159
```

### Understanding `.pyc` Files

- **`.pyc` files** are compiled Python bytecode generated automatically by Python.
- Located in the `__pycache__` directory within your project.
- Created when a module is first imported to speed up subsequent imports.
- Safe to delete; Python regenerates them automatically when needed.
- Not human-readable; computer-optimized for faster execution.

### Understanding `__init__.py`

- **`__init__.py`** marks a directory as a Python package.
- Can be empty or contain initialization code for the package.
- Runs when the package is imported.
- Allows organizing multiple modules in a directory.

**Example Package Structure:**
```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── __pycache__/
    ├── __init__.cpython-39.pyc
    ├── module1.cpython-39.pyc
    └── module2.cpython-39.pyc
```

**`__init__.py` Example:**
```python
# mypackage/__init__.py
print("Initializing mypackage")

from .module1 import function1
from .module2 import function2
```

Import the package:
```python
import mypackage  # Prints: Initializing mypackage
mypackage.function1()
```

> **Note:** In Python 3.3+, `__init__.py` is optional for namespace packages, but recommended for clarity.

## Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code in a modular and reusable way.

### Classes and Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Create an object
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Buddy says Woof!
```

### Key OOP Concepts

#### Encapsulation

Bundling data (attributes) and methods (functions) within a class. Control access using:
- `public`: Accessible from anywhere (default in Python)
- `protected`: Prefixed with `_` (convention; not enforced)
- `private`: Prefixed with `__` (name mangling applied)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

#### Inheritance

A class can inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat()
print(cat.speak())  # Meow
```

#### Polymorphism

Objects of different classes can respond to the same method call differently.

```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Woof, Meow
```

#### Abstraction

Hiding complex implementation details and exposing only essential features.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Engine started"
```

### Special Methods (Dunder Methods)

- `__init__`: Constructor; initializes objects
- `__str__`: String representation
- `__repr__`: Developer-friendly representation
- `__len__`: Length of object
- `__eq__`: Equality comparison
- `__add__`: Addition operator

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)  # (1, 2)
print(p1 + p2)  # (4, 6)
```

### Class Variables vs Instance Variables

- **Instance variables**: Unique to each object; defined in `__init__`
- **Class variables**: Shared across all instances; defined in class body

```python
class Counter:
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.count += 1

c1 = Counter("A")
c2 = Counter("B")
print(Counter.count)  # 2
```

### Static Methods and Class Methods

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def from_string(cls, value):
        return cls(int(value))

print(MathUtils.add(5, 3))  # 8
```

### Inheritance and `super()`

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

"""
Difference between Static Method vs Class Method:

Static Method:
    - Defined using @staticmethod decorator
    - Does not have access to instance (self) or class (cls)
    - Cannot access or modify instance or class attributes
    - Behaves like a regular function but belongs to the class namespace
    - Called on the class or instance, but receives no implicit first argument
    - Useful for utility functions related to the class conceptually

Class Method:
    - Defined using @classmethod decorator
    - Always receives the class (cls) as the first implicit argument
    - Can access and modify class attributes
    - Cannot directly access instance attributes
    - Called on the class or instance; if called on instance, still receives the class
    - Useful for factory methods and class-level operations
    - Can be inherited and overridden by subclasses

Key Differences:
    1. Access: Static methods have no implicit arguments; class methods receive cls
    2. State: Class methods can modify class state; static methods cannot
    3. Inheritance: Class methods are aware of inheritance; static methods are not
    4. Use Cases: Static for utility functions; class methods for alternative constructors
"""

## Dunder (Magic) Methods in Python

Dunder methods (double underscore methods) are special methods that enable objects to interact with built-in Python operations and syntax.

### Common Dunder Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `__init__` | Constructor; initializes object | `obj = MyClass()` |
| `__str__` | String representation for users | `print(obj)` |
| `__repr__` | Developer-friendly representation | `repr(obj)` |
| `__len__` | Length of object | `len(obj)` |
| `__getitem__` | Index access | `obj[0]` |
| `__setitem__` | Index assignment | `obj[0] = value` |
| `__delitem__` | Index deletion | `del obj[0]` |
| `__iter__` | Iterator protocol | `for item in obj:` |
| `__next__` | Next item in iteration | Used with iterators |
| `__eq__` | Equality comparison | `obj1 == obj2` |
| `__lt__` | Less than comparison | `obj1 < obj2` |
| `__le__` | Less than or equal | `obj1 <= obj2` |
| `__gt__` | Greater than comparison | `obj1 > obj2` |
| `__ge__` | Greater than or equal | `obj1 >= obj2` |
| `__ne__` | Not equal comparison | `obj1 != obj2` |
| `__add__` | Addition operator | `obj1 + obj2` |
| `__sub__` | Subtraction operator | `obj1 - obj2` |
| `__mul__` | Multiplication operator | `obj1 * obj2` |
| `__truediv__` | Division operator | `obj1 / obj2` |
| `__floordiv__` | Floor division operator | `obj1 // obj2` |
| `__mod__` | Modulus operator | `obj1 % obj2` |
| `__pow__` | Exponentiation operator | `obj1 ** obj2` |
| `__call__` | Make object callable | `obj()` |
| `__enter__` | Context manager entry | `with obj:` |
| `__exit__` | Context manager exit | `with obj:` |
| `__del__` | Destructor; cleanup | Called when object is deleted |
| `__hash__` | Hash value | `hash(obj)` |
| `__bool__` | Boolean value | `if obj:` |
| `__contains__` | Membership test | `item in obj` |

### Practical Examples

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return 2
    
    def __call__(self):
        return f"Called: ({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)           # Vector(1, 2)
print(v1 + v2)      # Vector(4, 6)
print(v1 == v2)     # False
print(len(v1))      # 2
print(v1())         # Called: (1, 2)
```

### Context Manager with `__enter__` and `__exit__`

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileHandler('data.txt') as f:
    content = f.read()
```

> Dunder methods allow seamless integration with Python's built-in functions and operators, making custom objects behave like native Python types.

## Built-in Dunder Variables in Python

Dunder variables (double underscore variables) provide metadata and context about modules, classes, and functions.

### Common Built-in Dunder Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `__name__` | Name of current module; `"__main__"` if script is executed directly | `if __name__ == "__main__":` |
| `__file__` | Path to the current file | `print(__file__)` |
| `__doc__` | Docstring of module, class, or function | `print(module.__doc__)` |
| `__dict__` | Namespace as a dictionary | `obj.__dict__` |
| `__class__` | Class of an object | `obj.__class__` |
| `__module__` | Module name where class/function is defined | `MyClass.__module__` |
| `__qualname__` | Qualified name of class/function | `MyClass.method.__qualname__` |
| `__package__` | Package name of current module | `print(__package__)` |
| `__cached__` | Path to `.pyc` file | `print(__cached__)` |
| `__loader__` | Loader object for the module | `print(__loader__)` |
| `__spec__` | Module specification | `print(__spec__)` |
| `__annotations__` | Type hints dictionary | `func.__annotations__` |
| `__code__` | Code object of function | `func.__code__` |
| `__globals__` | Global namespace dictionary | `func.__globals__` |
| `__locals__` | Local namespace dictionary | `locals()` |
| `__builtins__` | Built-in namespace | `__builtins__` |

### Practical Examples

```python
# __name__ and __file__
if __name__ == "__main__":
    print(f"Running {__file__} directly")

# __doc__
def my_function():
    """This is my function."""
    return "result"

print(my_function.__doc__)  # This is my function.

# __dict__
class Person:
    name = "Alice"

p = Person()
print(p.__dict__)  # Instance attributes

# __class__
obj = "string"
print(obj.__class__)  # <class 'str'>

# __annotations__
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```
## Exceptions in Python

Exceptions are errors that occur during program execution. Python handles exceptions using `try`, `except`, `else`, and `finally` blocks.

### Exception Handling Syntax

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero")
except ValueError:
    # Handle another exception
    print("Invalid value")
except Exception as e:
    # Catch any other exception
    print(f"Error: {e}")
else:
    # Runs if no exception occurred
    print("Division successful")
finally:
    # Always executes, regardless of exception
    print("Operation complete")
```

### Common Built-in Exceptions

| Exception | Cause | Example |
|-----------|-------|---------|
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `ValueError` | Wrong value type | `int("abc")` |
| `TypeError` | Wrong data type | `"text" + 5` |
| `IndexError` | Index out of range | `lst[10]` (list has 5 items) |
| `KeyError` | Dictionary key not found | `dict["missing_key"]` |
| `AttributeError` | Attribute doesn't exist | `obj.missing_attr` |
| `NameError` | Variable not defined | `print(undefined_var)` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `ImportError` | Module not found | `import missing_module` |
| `RuntimeError` | General runtime error | User-defined runtime issues |
| `RecursionError` | Too much recursion | Infinite recursive calls |
| `StopIteration` | Iterator exhausted | Raised when `next()` has no more items |

### Raising Custom Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Caught error: {e}")
```

### Creating Custom Exception Classes

```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"CustomError: {self.message}"

try:
    raise CustomError("Something went wrong")
except CustomError as e:
    print(e)
```

### Exception Hierarchy

Python exceptions follow a hierarchy:
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── StopIteration
    ├── GeneratorExit
    ├── ArithmeticError (ZeroDivisionError, OverflowError)
    ├── LookupError (IndexError, KeyError)
    ├── NameError
    ├── TypeError
    ├── ValueError
    ├── RuntimeError
    ├── OSError (FileNotFoundError, etc.)
    └── ... (many others)
```

### Best Practices

- Catch specific exceptions before general ones
- Avoid bare `except:` clauses; always specify exception type
- Use `finally` for cleanup operations (closing files, releasing resources)
- Provide meaningful error messages
- Don't suppress exceptions silently without good reason


## File Handling in Python

File handling involves reading, writing, and manipulating files. Python provides built-in functions and modules for efficient file operations.

### Opening and Closing Files

```python
# Basic file opening
file = open("filename.txt", "r")
content = file.read()
file.close()

# Using context manager (recommended)
with open("filename.txt", "r") as file:
    content = file.read()
# File automatically closes
```

### File Modes

| Mode | Purpose |
|------|---------|
| `"r"` | Read (default); file must exist |
| `"w"` | Write; creates new file or overwrites existing |
| `"a"` | Append; adds content to end of file |
| `"x"` | Create; fails if file already exists |
| `"b"` | Binary mode; can be combined with others (`"rb"`, `"wb"`) |
| `"t"` | Text mode (default); can be combined with others |
| `"+"` | Read and write; can be combined (`"r+"`, `"w+"`) |

### Reading Files

```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines as list
with open("file.txt", "r") as file:
    lines = file.readlines()

# Read single line
with open("file.txt", "r") as file:
    first_line = file.readline()
```

### Writing Files

```python
# Write to file
with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Write multiple lines
with open("file.txt", "w") as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)

# Append to file
with open("file.txt", "a") as file:
    file.write("Appended line\n")
```

### Working with JSON Files

JSON (JavaScript Object Notation) is a lightweight data format for storing and exchanging structured data.

```python
import json

# Write to JSON file
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read from JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])  # Alice

# Convert string to JSON object
json_string = '{"name": "Bob", "age": 25}'
parsed_data = json.loads(json_string)

# Convert Python object to JSON string
json_output = json.dumps(data, indent=2)
print(json_output)
```

### Working with CSV Files

CSV (Comma-Separated Values) stores tabular data. Use the `csv` module for safe parsing.

```python
import csv

# Write to CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read from CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read as dictionaries (with headers)
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])

# Write dictionaries to CSV
records = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles"}
]

with open("data.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
```

### File Operations

```python
import os

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

# Get file size
size = os.path.getsize("file.txt")
print(f"File size: {size} bytes")

# Rename file
os.rename("old_name.txt", "new_name.txt")

# Delete file
os.remove("file.txt")

# Get current working directory
cwd = os.getcwd()

# List files in directory
files = os.listdir(".")

# Create directory
os.makedirs("new_folder", exist_ok=True)
```

### Best Practices

- Always use context managers (`with` statement) to ensure files close properly
- Handle exceptions when reading/writing files
- Use `newline=""` parameter when writing CSV files to avoid extra blank lines
- Use `json.dumps()` and `json.loads()` for string conversion
- Use `csv.DictReader` and `csv.DictWriter` for structured data
- Specify encoding explicitly when needed: `open("file.txt", "r", encoding="utf-8")`
## Pickling in Python

Pickling is the process of converting Python objects into byte streams (serialization). Unpickling reverses this process, reconstructing objects from byte streams. The `pickle` module enables object serialization for storage or transmission.

### Basic Pickling and Unpickling

```python
import pickle

# Create an object
data = {"name": "Alice", "age": 30, "items": [1, 2, 3]}

# Pickle to bytes
pickled_data = pickle.dumps(data)
print(pickled_data)  # Binary representation

# Unpickle from bytes
unpickled_data = pickle.loads(pickled_data)
print(unpickled_data)  # {"name": "Alice", "age": 30, "items": [1, 2, 3]}
```

### Pickling to Files

```python
import pickle

# Write object to file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Read object from file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
```

### Pickling Custom Objects

```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Pickle custom object
person = Person("Bob", 25)
pickled = pickle.dumps(person)

# Unpickle custom object
unpickled_person = pickle.loads(pickled)
print(unpickled_person)  # Person(name=Bob, age=25)
```

### Pickle Protocols

Different pickle protocols offer varying levels of compatibility and efficiency:

| Protocol | Version | Features |
|----------|---------|----------|
| 0 | Human-readable ASCII | Slow; compatible with all Python versions |
| 1 | Legacy binary | Binary format; Python 1.5+ |
| 2 | Efficient binary | Optimized for Python 2.3+ |
| 3 | Binary | Python 3.0+; default in Python 3 |
| 4 | Binary | Python 3.4+; handles large objects efficiently |
| 5 | Binary | Python 3.8+; supports out-of-band data |

```python
# Specify protocol
pickled = pickle.dumps(data, protocol=4)

# Default protocol (highest available)
pickled = pickle.dumps(data)
```

### Pickle vs JSON

| Aspect | Pickle | JSON |
|--------|--------|------|
| Format | Binary | Text |
| Security | Unsafe; code execution risk | Safe |
| Language Support | Python only | All languages |
| Object Types | Most Python objects | Basic types (dict, list, str, int) |
| Human Readable | No | Yes |
| Use Case | Python-to-Python serialization | Data interchange |

### Security Considerations

⚠️ **Warning:** Never unpickle untrusted data. Pickling can execute arbitrary code during unpickle operations.

```python
# Safe approach: validate source before unpickling
import pickle

# Only unpickle data from trusted sources
with open("trusted_data.pkl", "rb") as file:
    data = pickle.load(file)
```

### Best Practices

- Use `pickle` for internal Python serialization only
- Use `json` for data interchange or untrusted sources
- Always use binary mode (`"wb"`, `"rb"`) when pickling to/from files
- Specify protocol version for compatibility across Python versions
- Consider custom `__getstate__()` and `__setstate__()` for complex objects
- Don't pickle sensitive data (passwords, keys); use secure methods instead

## Database Connectivity with MySQL in Python

### Installing MySQL Connector

```python
# Install using pip
pip install mysql-connector-python
```

### Basic Connection to MySQL

```python
import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

# Create cursor
cursor = connection.cursor()

# Close connection
cursor.close()
connection.close()
```

### Executing Queries

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)

cursor = connection.cursor()

# CREATE table
create_table = """
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
"""
cursor.execute(create_table)

# INSERT data
insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
data = ("Alice", "alice@example.com")
cursor.execute(insert_query, data)
connection.commit()

# SELECT data
select_query = "SELECT * FROM users"
cursor.execute(select_query)
results = cursor.fetchall()
for row in results:
    print(row)

# UPDATE data
update_query = "UPDATE users SET email = %s WHERE name = %s"
cursor.execute(update_query, ("newemail@example.com", "Alice"))
connection.commit()

# DELETE data
delete_query = "DELETE FROM users WHERE name = %s"
cursor.execute(delete_query, ("Alice",))
connection.commit()

cursor.close()
connection.close()
```

### Using Context Manager (Recommended)

```python
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydb"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
finally:
    cursor.close()
    connection.close()
```

### Fetching Results

```python
cursor.execute("SELECT * FROM users")

# Fetch one row
one_row = cursor.fetchone()

# Fetch all rows
all_rows = cursor.fetchall()

# Fetch specific number of rows
few_rows = cursor.fetchmany(5)

# Get column names
cursor.execute("SELECT * FROM users")
column_names = [desc[0] for desc in cursor.description]
```

### Parameterized Queries (Prevent SQL Injection)

```python
# Safe: using parameterized queries
query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, ("Alice",))

# Unsafe: string concatenation
# query = f"SELECT * FROM users WHERE name = '{name}'"  # Avoid!
```

### Batch Insert

```python
data = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
]

query = "INSERT INTO users (name, email) VALUES (%s, %s)"
cursor.executemany(query, data)
connection.commit()
```

### Error Handling

```python
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydb"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    
except Error as e:
    print(f"Error: {e}")
    
finally:
    if cursor:
        cursor.close()
    if connection.is_connected():
        connection.close()
```

### Connection Pooling

```python
from mysql.connector import pooling

# Create connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)

# Get connection from pool
connection = connection_pool.get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

cursor.close()
connection.close()
```
