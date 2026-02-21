# **Object-Oriented Programming (OOP) Concepts in Python**

This repository contains my practice implementations and notes on important OOP concepts in Python.

### **Aggregation**

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