import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print("Time taken by", func.__name__, time.time() - start, "secs")

    return wrapper


@timer
def hello():
    print("Hello world")
    time.sleep(2)


@timer
def display():
    print("Displaying something")
    time.sleep(4)


hello()
display()
