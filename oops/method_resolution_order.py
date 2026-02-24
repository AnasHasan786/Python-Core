class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone class constructor!!")
        self.__price = price
        self.__brand = brand
        self.__camera = camera

    def buy(self):
        print("Buying a phone")


class Product:

    def buy(self):
        print("Buying a product")


class SmartPhone(Product, Phone):
    pass


s = SmartPhone(45000, "vivo", 48)
s.buy()
