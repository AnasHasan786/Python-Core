# using with keyword

with open("/content/sample.txt", "w") as f:
    f.write("Salman Khan")


# trying to read a file with 'with' keyword
with open("/content/sample_1.txt", "r") as f:
    print(f.read())


# moving within a file
with open("sample_1.txt", "r") as f:
    print(f.read(10))
    print(f.read(10))


# Creating a big file
big_L = ["hello world" for i in range(1000)]

with open("big.txt", "w") as f:
    f.writelines(big_L)


with open("big.txt", "r") as f:

    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end="***")
        f.read(chunk_size)
