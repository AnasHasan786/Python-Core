class MyException(Exception):

    def __init__(self, message):
        print(message)


class Bank:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise MyException("Invalild amount!!")
        if self.balance < amount:
            raise MyException("Insufficient funds!!")
        self.balance = self.balance - amount


obj = Bank(10000)
try:
    obj.withdraw(6371)
except MyException as e:
    pass
else:
    print(obj.balance)
