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
