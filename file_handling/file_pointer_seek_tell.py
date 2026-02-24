with open("big.txt", "r") as f:
    print(f.read(10))
    print(f.tell())
    f.seek(15)
    print(f.read(10))


# seek during write
with open("sample.txt", "w") as f:
    f.write("Hello")
    f.seek(0)
    f.write("X")
