def my_range(start, end):

    for i in range(start, end):
        yield i


gen = my_range(15, 26)

for i in gen:
    print(i)
