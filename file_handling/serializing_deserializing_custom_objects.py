class Person:

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person = Person("Ajay", "Singh", 23, "male")


# As a string
import json


def show_object(person):
    if isinstance(person, Person):
        return "{} {} age -> {} gender -> {}".format(
            person.fname, person.lname, person.age, person.gender
        )


with open("demo.json", "w") as f:
    json.dump(person, f, default=show_object)


# As a dict
def show_object(person):
    if isinstance(person, Person):
        return {
            "name": person.fname + " " + person.lname,
            "age": person.age,
            "gender": person.gender,
        }


with open("demo.json", "w") as f:
    json.dump(person, f, default=show_object, indent=4)


# deserializing
with open("demo.json", "r") as f:
    d = json.load(f)
    print(d)
    print(type(d))
