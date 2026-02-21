class Person:

    def __init__(self, name, gender, address):
        self.__name = name
        self.__gender = gender
        self.__address = address

    def print(self):
        print(
            self.__address.get_city(),
            self.__address.get_pin_code(),
            self.__address.get_state(),
        )

    def edit_profile(self, new_name, new_city, new_pin_code, new_state):
        self.__name = new_name
        self.__address.edit_address(new_city, new_pin_code, new_state)


class Address:

    def __init__(self, city, pin_code, state):
        self.__city = city
        self.__pin_code = pin_code
        self.__state = state

    def get_city(self):
        return self.__city

    def get_pin_code(self):
        return self.__pin_code

    def get_state(self):
        return self.__state

    def edit_address(self, new_city, new_pin_code, new_state):
        self.__city = new_city
        self.__pin_code = new_pin_code
        self.__state = new_state


add = Address("mumbai", 120021, "maharashtra")
p = Person("ajay", "male", add)
p.print()

p.edit_profile("vijay", "gurgaon", 110011, "haryana")
p.print()
