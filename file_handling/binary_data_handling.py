# working with binary file
with open("/content/cat.jpg", "rb") as f:
    with open("/content/cat_copy.jpg", "wb") as wf:
        wf.write(f.read())


# working with other data types
with open("sample.txt", "w") as f:
    f.write("5")


with open("sample.txt", "r") as f:
    print(int(f.read()) + 5)


# working with more complex types
d = {"name": "ajay", "age": 23, "gender": "male"}

with open("sample.txt", "w") as f:
    f.write(str(d))


with open("sample.txt", "r") as f:
    print(f.read())
