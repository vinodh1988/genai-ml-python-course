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