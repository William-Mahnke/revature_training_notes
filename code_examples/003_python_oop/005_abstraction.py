from abc import ABC, abstractmethod

# Abstract base class — cannot be instantiated directly
class Shape(ABC):

    @abstractmethod
    def area(self):
        """Every shape must implement area()."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape must implement perimeter()."""
        pass

    # Concrete method — shared by all shapes, not overridden
    def describe(self):
        print(f"I am a {self.__class__.__name__}.")
        print(f"  Area:      {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")

# Cannot instantiate the abstract class directly
# s = Shape()   # TypeError: Can't instantiate abstract class

# Concrete subclass — must implement all abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Can instantiate concrete subclasses
c = Circle(5)
r = Rectangle(4, 6)

c.describe()
# I am a Circle.
#   Area:      78.54
#   Perimeter: 31.42

r.describe()
# I am a Rectangle.
#   Area:      24.00
#   Perimeter: 20.00

# Abstraction in action — caller doesn't care which shape it is
shapes = [Circle(3), Rectangle(2, 5), Circle(7)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.2f}")


# What happens if a subclass forgets to implement an abstract method?
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    # perimeter() not implemented — Python will enforce this

t = Triangle(3, 4)
# TypeError: Can't instantiate abstract class Triangle
# without an implementation for abstract method 'perimeter'