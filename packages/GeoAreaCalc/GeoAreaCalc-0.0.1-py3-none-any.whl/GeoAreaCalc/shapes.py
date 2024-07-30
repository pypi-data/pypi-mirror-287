import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    """Calculator for Circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Calculator for a triangle with known three sides and checking for a right angle."""
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def is_right_triangle(self):
        """Check if the triangle is right."""
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


