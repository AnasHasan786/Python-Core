## **Exception Handling in Python**

Exception handling is a mechanism in Python that allows a program to handle runtime errors gracefully without crashing.

Instead of stopping execution, Python provides special blocks to detect, handle, and manage errors properly.

**Why do we need Exception Handling?**

- Prevents program crashes
- Improves user experience
- Helps in debugging
- Maintains normal program flow
- Allows custom error messages

**Common Python Exceptions**

Below are some frequently occuring exceptions in Python along with simple examples.

#### **1. IndexError**: `IndexError` is thrown when trying to access an element at an invalid index.

```python
L = [1, 2, 3]
L[100]   # IndexError
```

**Explanation**: The list contains only 3 elements (index 0-2). Index 100 does not exist.

#### **2. ModuleNotFoundError**: `ModuleNotFoundError` is thrown when Python cannot find the specified module.

```python
import mathi    # ModuleNotFoundError
```

**Explanation**: There is no module named `mathi`. The correct module is `math`.

#### **3. KeyError**: `KeyError` is thrown when a dictionary key does not exist.

```python
d = {'name': 'ajay'}
d['age']       # KeyError
```

**Explanation**: The dictionary does not contain the key `age`.

#### **4. TypeError**: `TypeError` occurs when an operation is applied to an inappropriate data type.

```python
1 + 'a'     # TypeError
```

**Explanation**: You cannot add an integer and a string together.

#### **5. ValueError**: `ValueError` occurs when a function receives the correct type but an inappropriate value.

```python
int('a')     # ValueError
```

**Explanation**: `int()` expects a numeric string, but `a` cannot be converted to an integer.

#### **6. NameError**: `NameError` occurs when a variable or name is not defined.

```python
print(k)    # NameError
```

**Explanation**: The variable `k` has not been declared.

#### **7. AttributeError**: `AttributeError` occurs when an invalid attribute or method is used.

```python
L = [1, 2, 3]
L.upper()  # AttributeError
```

**Explanation**: List do not have an `upper()` method. That method belongs to strings.

### **Basic Example**

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a number.")
```

### **The `try-except-else-finally` structure**

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
    file.close()
finally:
    print("Execution completed.")
```

### **Raising Exceptions Manually**

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

### **Creating Custom Exceptions**

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid age provided")
```

In summary, exception handling makes Python programs more robust, user-friendly, and maintainable. It ensures that errors are managed properly without breaking the entire application.
