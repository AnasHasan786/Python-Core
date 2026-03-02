class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Hi my name is ", self.name, " and I am ", self.age, " years old.")


p = Person("Ajay", 23)

# pickle dump
import pickle

with open("person.pkl", "wb") as f:
    pickle.dump(p, f)

# pickle load
import pickle

with open("person.pkl", "rb") as f:
    p = pickle.load(f)

p.display_info()
