# **File Handling + Serialization and Deserialization**

**Types of data used for I/O:-**

- `Text`: '12345' as a sequence of unicode chars.
- `Binary`: 12345 as a sequence of bytes of its binary equivalent.

There are 2 file types to deal with:-

- `Text files`: All program files are text files.
- `Binary files`: Images, music, video, exe files.

**How File I/O is done in most programming languages:-**

- Open a file
- Read/Write data
- Close the file

**Context Manager (with keyword)**

```python
# writing in a file
with open('/content/sample.txt', 'w') as f:
    f.write('Salman Khan')

# trying to read a file with 'with' keyword
with open('/content/sample_1.txt', 'r') as f:
    print(f.read())
```

- It's a good idea to close a file after usage as it will free up the resources.
- If we don't close it, garbage collector would eventually close it.
- `with` keyword closes the file as soon as the usage is over.

**seek and tell function**

seek function can set the starting point of reading a file from the desired position we want.

```python
with open('big.txt', 'r') as f:
    print(f.read(10))
    f.seek(15)
    print(f.read(10))
```

tell function denotes the current position from where reading has to start again or reading ends if there is no data.

```python
with open('big.txt', 'r') as f:
  print(f.read(10))
  print(f.tell())
```

**Problems with working in text mode**

- can't work with binary files like images.
- not good for other data types like int/float/list/tuples.

```python
# working with binary file
with open('/content/cat.jpg', 'rb') as f:
    with open('/content/cat_copy.jpg', 'wb') as wf:
        wf.write(f.read())
```

### **Serialization and Deserialization**

- `Serialization`: process of converting python data types to JSON format.
- `Deserialization`: process of converting JSON to python data types.

```python
# serialization 
import json

d = {
    'name': 'ajay',
    'age': 23,
    'gender': 'male'
}

with open('demo.json', 'w') as f:
    json.dump(d, f, indent=4)

# deserialization
with open('demo.json', 'r') as f:
    d = json.load(f)
    print(d)
    print(type(d))
```

**Pickling**

`Pickling` is the process whereby a Python object hierarchy is converted into a byte stream, and `unpickling` is the inverse operation, whereby a byte stream (from a binary file or byte-like object) is converted back into an object hierarchy.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is ', self.name, ' and I am ', self.age, ' years old.')

p = Person('Ajay', 23)

# pickle dump
import pickle

with open('person.pkl', 'wb') as f:
    pickle.dump(p, f)

# pickle load
with open('person.pkl', 'rb') as f:
    p = pickle.load(f)

p.display_info()
```

**Note**: `Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.`