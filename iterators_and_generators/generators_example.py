def gen_demo():

    yield "first statement"
    yield "second statement"
    yield "third statement"


gen = gen_demo()

for i in gen:
    print(i)
