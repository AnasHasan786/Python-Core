## **Python fundamentals**

The `fundamentals` folder provides practical examples of the core concepts that form the foundation of Python programming. These examples are designed to help learners understand how the language works internally and how its basic features are used in real programs. Mastering these fundamentals makes it easier to progress to advanced areas such as software development, data analysis, machine learning, and AI systems.

### **1. Python Output**

Python provides the `print()` function to display output on the console.

**Basic Output**

```python
# Python is a case sensitive language
print('Hello World!!')
```

**Output:** Hello World

**Custom Separator**

The `sep` parameter changes how values are separated.

```python
print('Hello', 1, 4.5, True, sep='/')
```

**Output:** Hello/1/4.5/True

**Controlling Line Ending**

The `end` parameter controls what appears after the print statement.

```python
print('Hello', end='-')
print('World!!')
```

**Output:** Hello-World!!

### **2. Data Types**

Python supports multiple built-in data types.

**Integer**

```python
print(8)
print(1e308)
```

**Float/Decimal**

```python
print(8.55)
print(1.7e308)
```

**Boolean**

```python
print(True)
print(False)
```

**String (Text)**

```python
print('Hello World!!')
```

**Complex Number**

```python
print(5+6j)
```

**List**

```python
print([1, 2, 3, 4, 5])
```

**Tuple**

```python
print((1, 2, 3, 4, 5))
```

**Set**

```python
print({1, 2, 3, 4, 5})
```

**Dictionary**

```python
print({'Name': 'Ajay', 'Gender': 'M'})
```

### **3. Variables**

Variables are used to store data values.

```python
a = 5
b = 6
print(a + b)
```

**Note:-**
1. `Dynamic Typing`: Here we don't have to specify the data type of variable (like in C++), Python automatically detects the data type here.

2. `Static Typing`: Here we have to specify the data type of variable.

Python supports `Dynamic Typing` while other languages like C, C++, Java supports `Static Typing`.

**Dynamic and Static Binding**

```python
# Dynamic Binding
a = 5
print(a)
a = 'Anas'
print(a)

# Static Binding
# int a = 5;
```

**`Dynamic Binding`:** With this feature, a variable of any type can be assigned value of any other type also later on.

**`Static Binding`:** This feature don't allow us to change the value of variable to any other data type value.

Python supports Dynamic Binding while other languages like C, C++, Java supports Static Binding.

### **4. Keywords & Identifiers**

**Keywords:**: Keywords are `reserved words` in Python that cannot be used as variable names.

Examples: if, else, while, for, class, return

**Identifiers:** Identifiers are names given to variables, functions, classes, etc.

Example:

name = "Anas"

**Rules for creating Identifiers**

1. Cannot start with a digit.
2. Only _ is allowed as a special character.
3. Cannot use Python keywords.
4. Should be meaningful and readable.

### **5. User Input**

The `input()` function allows users to enter data.

```python
name = input('Enter your name: ')
print(name)
```

### **6. Type Conversion**

Type conversion means converting one data type into another.

**Implicit Type Conversion**

Handled automatically by Python.

```python
print(5 + 5.6)
```

**Output:** 10.6

**Explicit Type Conversion**

Handled manually by the programmer.

```python
print(int(4.5))
```

**Output:** 4

### **7. Literals**

Literals are fixed values assigned to variables.

**Binary Literal**

```python
a = 0b1010
print(a)
```

**Decimal Literal**

```python
b = 100
print(b)
```

**Complex Literal**

```python
x = 3.14j
print(x.real, x.imag)
```

**None Literal**

```python
a = None
print(a)
```

