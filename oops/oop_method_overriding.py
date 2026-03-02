class Phone:

    def __init__(self, price, brand, camera):
        print("Inside parent class constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = camera

    def buy(self):
        return "Buying a phone"


class SmartPhone(Phone):

    def buy(self):
        return "Buying a smartphone"


s = SmartPhone(45000, "Vivo", "Good")
s.buy()
