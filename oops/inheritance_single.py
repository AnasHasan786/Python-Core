class Phone:

    def __init__(self, price, brand, camera):
        print("Inside the parent class constructor!!")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        return "Buying a phone"


class User(Phone):
    pass


u = User(56000, "Vivo", 48)
u.buy()
