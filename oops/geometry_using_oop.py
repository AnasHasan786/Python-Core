class Point:

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __str__(self):
        return "<{}, {}>".format(self.x_coord, self.y_coord)

    def euclidean_distance(self, other):
        return (
            (other.x_coord - self.x_coord) ** 2 + (other.y_coord - self.y_coord) ** 2
        ) ** 0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(0, 0))


class Line:

    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def __str__(self):
        a = f"{self.A}x"

        b = f" + {self.B}y" if self.B >= 0 else f" - {abs(self.B)}y"
        c = f" + {self.C}" if self.C >= 0 else f" - {abs(self.C)}"

        return a + b + c + " = 0"

    def point_on_line(self, point):
        if self.A * point.x_coord + self.B * point.y_coord + self.C == 0:
            return "Point {} lies on the {}".format(point, self)
        else:
            return "Point {} does not lies on the {}".format(point, self)

    def shortest_distance(self, point):
        return (
            abs(self.A * point.x_coord + self.B * point.y_coord + self.C)
            / (self.A**2 + self.B**2) ** 0.5
        )

    def intersect(self, other):
        det = self.A * other.B - self.B * other.A

        if det != 0:
            return "Lines are intersecting!!"
        elif (
            self.A * other.C == self.C * other.A and self.B * other.C == self.C**other.B
        ):
            return "Lines are coincident!!"
        else:
            return "Lines are parallel!!"


p1 = Point(2, 3)
p2 = Point(2, 6)

l1 = Line(2, 3, -5)
l2 = Line(3, 4, 2)
print(l1.point_on_line(p2))
print(l1.shortest_distance(p2))
print(l1.intersect(l2))
