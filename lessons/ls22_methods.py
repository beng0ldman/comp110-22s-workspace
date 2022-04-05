"""More class practice/Operator Oberload (LS26)."""

from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special method to represent object as string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        """Means we can do a * 2.0 instead of a.scale(2.0)."""
        """Also means you can take out scale method."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: Point) -> Point:
        """Overload the addition operator for Point + float."""
        return Point(self.x + factor.x, self.y + factor.y)

    # def scale(self, factor: float) -> Point:
    #     """Scale a Point's attributes by a factor."""
    #     return Point(self.x * factor, self.y * factor)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])
