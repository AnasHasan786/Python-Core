class Phone:

    def __init__(self, price, brand, camera):
        print("Inside parent class constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("Inside child class constructor")
        super().__init__(price, brand, camera)
        self.__os = os
        self.__ram = ram
        print("Inside child class constructor")


s = SmartPhone(56000, "vivo", "good", "funtouch", 12)
