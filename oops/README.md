# **Object-Oriented Programming (OOP) Concepts in Python**

This repository contains my practice implementations and notes on important OOP concepts in Python.

### **<u>Aggregation</u>**

Aggregation is a relationship between two classes where one class uses or contains an object of another class, but both can exist independently.

**Note**: `The container class should not access private members of the other class directly (it should use public methods).`

**Real-Life Examples**

- A Department has Teachers.
- If the Department is deleted, Teachers can still exist.

So:

- Department -> has a -> Teacher
- But Teacher does not depend on Department to exist.

**Structural Example**

```python
class Teacher:
    def __init__(self, name):
        self.name = name
    
class Department:
    def __init__(self, teacher):
        self.teacher = teacher

t1 = Teacher("Vijay")
dept = Department(t1)

print(dept.teacher.name)

```

**Class Diagram**

The diagram below demonstrates aggregation using another example (`Customer` and `Address`) for clarity.

![Aggregation Class Diagram](images/aggregation_class_diagram.png)

#### **Explanation**

- `Customer` has an `Address` (has-a relationship).
- The hollow diamond represents aggregation.
- Both classes can exist independently.


### **<u>Inheritance</u>**

Inheritance is an OOP concept where one class acquired the properties and methods of another class. It represents an is-a relationship.

**Key idea of inheritance**

- It promotes code reusability.
- Helps in building relationships.
- Child class can reuse and extend parent class functionality.

**Basic Example**

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")
    
class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
```
**Class Diagram**

The diagram below demonstrates inheritance for visual clarity.

![Inheritance Class Diagram](images/inheritance_class_diagram.png)

**Types of Inheritance**

1. `Single Inheritance:` One child class inherits from one parent class.
2. `Multiple Inheritance:` One child class inherits from more than one parent class.
3. `Multiple Inheritance:` A class inherits from a class that is already a child class.
4. `Hierarchical Inheritance:` Multiple child classes inherit from one parent class.