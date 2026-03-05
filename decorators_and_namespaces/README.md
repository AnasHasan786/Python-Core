## **Decorators & Namespaces**

### **Decorators**

A decorator is a function that modifies or extends the behavior of another function without changing its actual code.

Decorators use the `@decorator_name` syntax.

They are commonly used for:

- Logging
- Authentication
- Access control
- Performance measurement
- Caching

#### **Basic Decorator Example**

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
```

#### **How Decorators Work**

The decorator syntax:

```python
@my_decorator
def say_hello():
    print("Hello")
```

is equivalent to:

```python
say_hello = my_decorator(say_hello)
```

#### **Decorator with Arguments**

If the decorated function takes parameters:

```python
def my_decorator(func):
    def wrapper(name):
        print("Before function call")
        func(name)
        print("After function call")
    return wrapper


@my_decorator
def greet(name):
    print(f"Hello {name}")


greet("Anas")
```

#### **Using `*args` and `**kwargs**`**

Best practice is to allow any arguments.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper
```

#### **Built-in Decorators**

Python provides several built-in decorators:

| Decorator | Purpose |
|--------|--------|
| `@staticmethod` | Defines a static method in a class |
| `@classmethod` | Defines a class method |
| `@property` | Allows a method to be accessed like an attribute |

Example:

```python
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

### **Namespaces**

A namespace is a container that holds names (identifiers) and their corresponding objects.

It prevents name conflicts in programs.

Example:

```python
x = 10
```

Here:

- `x` → name
- `10` → object


#### Types of Namespaces

Python mainly has four namespaces:

1. Built-in Namespace
2. Global Namespace
3. Enclosing Namespace
4. Local Namespace

This is often remembered using the `LEGB Rule`.

#### LEGB Rule

Python searches for variables in this order:

| Level | Description |
|------|-------------|
| **L** | Local |
| **E** | Enclosing |
| **G** | Global |
| **B** | Built-in |

##### **1. Local Namespace**

Variables defined inside a function.

```python
def my_function():
    x = 5
    print(x)
```

`x` exists only inside `my_function`.

##### **2. Enclosing Namespace**

Occurs with nested functions.

```python
def outer():
    x = "outer variable"

    def inner():
        print(x)

    inner()

outer()
```

`inner()` accesses the enclosing variable `x`.

##### **3. Global Namespace**

Variables defined at the top level of a module.

```python
x = 100

def show():
    print(x)

show()
```

##### **4. Built-in Namespace**

Contains Python's built-in functions like:

```
print()
len()
sum()
type()
```

Example:

```python
print(len("Python"))
```

### Viewing Namespaces

#### Local Namespace

```python
locals()
```

#### Global Namespace

```python
globals()
```

Example:

```python
x = 10
print(globals())
```

##### Modifying Global Variables

Use the `global` keyword.

```python
x = 5

def change():
    global x
    x = 20

change()
print(x)
```

Output:

```
20
```

### Summary

| Concept | Description |
|------|-------------|
| Decorators | Modify function behavior without changing its code |
| Namespace | Mapping between names and objects |
| LEGB Rule | Order Python follows to resolve variables |