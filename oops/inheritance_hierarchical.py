class Phone:

  def __init__(self, price, brand, camera):
    print("Inside phone class constructor!!")
    self.__price = price
    self.__brand = brand
    self.__camera = camera
  
  def buy(self):
    print("Buying a phone")

class SmartPhone(Phone):
  pass

class KeypadPhone(Phone):
  pass

s = SmartPhone(65000, 'oppo', 'good')
s.buy()
k = KeypadPhone(2300, 'nokia', 'na')
k.buy()