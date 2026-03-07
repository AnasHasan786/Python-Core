def my_own_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


a = [1, 2, 3]
b = range(1, 11)
c = (1, 2, 3)
d = {1, 2, 3}
e = {0: 1, 1: 1}

print(my_own_loop(a))
print(my_own_loop(b))
print(my_own_loop(c))
print(my_own_loop(d))
print(my_own_loop(e))
