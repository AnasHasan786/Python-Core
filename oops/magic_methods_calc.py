class Calc:

    def __init__(self, x):
        self.num = x

    def __add__(self, other):
        return Calc(self.num + other.num)

    def __sub__(self, other):
        return Calc(self.num - other.num)

    def __mul__(self, other):
        return Calc(self.num * other.num)

    def __truediv__(self, other):
        return Calc(self.num / other.num)

    def __mod__(self, other):
        return Calc(self.num % other.num)

    def __pow__(self, other):
        return Calc(self.num**other.num)

    def __str__(self):
        return str(self.num)


obj1 = Calc(4)
obj2 = Calc(3)
obj3 = Calc(2)

print(obj1 + obj2 + obj3)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)
print(obj1 % obj2)
print(obj1**obj2)
