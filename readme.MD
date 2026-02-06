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