## **Iterators and Generators**

### **Iterators**

Before understanding iterators, we mush understand **what `iteration` is?**
iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

An iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory.

**What is Iterable?**

Iterable is an object, which one can iterate over. It generates an iterator when passed to `iter()` method.

**Basic example of iterable and iterator**

```python
L = [1, 2, 3]
type(L)

# L is an iterable
type(iter(L))

# iter(L) ----> iterator
```

Important points to keep in mind are:-

- Every `iterator` is also an `iterable`.
- Not all `iterables` are `iterators`.
- Every iterable has an `iter function`.
- Every iterator has both `iter function` as well as `next function`.

**Understanding how `for loop` works**

First, we have to fetch the iterator from the iterable, and then use next on iterator.

This below example code will make things more clear.

```python
num = [1, 2, 3]

# step1 ---> fetch the iterator
iter_num = iter(num)

# step2 ---> next
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
```

**Another important concept of Iterators**

```python
num = [1, 2, 3]
iter_obj = iter(num)

print('Address of iterator 1: ', id(iter_obj))

iter_obj2 = iter(iter_obj)
print('Address of iterator 2: ', id(iter_obj2))
```

### **Generators**

Python `generators` are a simple way of creating iterators.

```python
def gen_demo():
    
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()

for i in gen:
    print(i)
```

**Difference between `return` and `yield`**

The difference between `return` and `yield` is:-

return ends the function execution immediately and sends a value back to the caller.

Once return is executed:

1. the function terminates
2. the function cannot resume from that point.

yield pauses the function and returns a value, but remembers the function's state so it can continue later.

Functions that use `yield` become generators.

```python
def square(num):
    for i in range(1, num+1):
        yield i**2

gen = square(10)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
```

### **Generator Expression**

```python
# List comprehension  ------------------> Basic way
L = [i**2 for i in range(1, 101)]


# generator way
gen = (i**2 for i in range(1, 101))

for i in gen:
    print(i)
```