class Phone:

  def __init__(self, price, brand, camera):
    print("Inside phone class constructor!!")
    self.__price = price
    self.__brand = brand
    self.__camera = camera

  def buy(self):
    print("Buying a phone")

class Product:

  def review(self):
    print("Customer product review")

class SmartPhone(Phone, Product):
  pass

s = SmartPhone(45000, 'vivo', 48)
s.buy()
s.review()