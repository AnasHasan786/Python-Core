class Product:

    def review(self):
        print("Producing customer review")


class Phone(Product):

    def __init__(self, price, brand, camera):
        self.__price = price
        self.__brand = brand
        self.__camera = camera

    def buy(self):
        print("Buying a phone")


class User(Phone):
    pass


u = User(45000, "vivo", "good")
u.buy()
u.review()
