from abc import ABC, abstractmethod

# A decorator modifies the behavior of a function
# or method. Built-in decorators are applied using
# the @ symbol directly above a method definition.
# 

# ═══════════════════════════════════════════════════════
# @staticmethod
# A method that belongs to the class but does NOT
# need access to the class (cls) or instance (self)
# Think of it as a regular function that lives
# inside a class for organizational purposes
# ═══════════════════════════════════════════════════════

class MathHelper:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


# ── Calling a static method ────────────────────────────
# Can be called on the class directly — no instance needed

print(MathHelper.add(5, 3))         # 8
print(MathHelper.is_even(4))        # True
print(MathHelper.is_even(7))        # False

# Can also be called on an instance, but calling
# directly on the class is the more common pattern
helper = MathHelper()
print(helper.add(10, 5))            # 15


# ═══════════════════════════════════════════════════════
# @classmethod
# A method that belongs to the CLASS itself rather
# than an instance. It receives the class (cls) as
# its first argument instead of self.
# Commonly used as an alternative constructor
# ═══════════════════════════════════════════════════════
class Employee:

    company = "Acme Corp"           # class variable — shared by all instances

    def __init__(self, emp_id, emp_name, emp_title):
        self.emp_id    = emp_id
        self.emp_name  = emp_name
        self.emp_title = emp_title

    def describe(self):
        return f"{self.emp_id} — {self.emp_name} — {self.emp_title}"

    @classmethod
    def get_company(cls):
        return f"Company: {cls.company}"    # accesses the class variable via cls

    @classmethod
    def from_string(cls, emp_string):
        # ── Alternative constructor ────────────────────
        # Allows creating an Employee from a formatted
        # string instead of individual arguments
        emp_id, emp_name, emp_title = emp_string.split(",")
        return cls(emp_id.strip(), emp_name.strip(), emp_title.strip())


# ── Calling a class method ─────────────────────────────
# Called on the class directly — no instance needed

print(Employee.get_company())           # Company: Acme Corp

# ── Using the alternative constructor ─────────────────
emp_data = "100, Joseph, Developer"
e = Employee.from_string(emp_data)
print(e.describe())                     # 100 — Joseph — Developer

# ── Standard constructor still works as normal ─────────
e2 = Employee(101, "Alice", "Manager")
print(e2.describe())                    # 101 — Alice — Manager


# ═══════════════════════════════════════════════════════
# @abstractmethod
# Forces subclasses to implement specific methods
# A class using @abstractmethod must inherit from ABC
# (Abstract Base Class). You cannot instantiate an
# abstract class directly — it must be subclassed
# ═══════════════════════════════════════════════════════

class Shape(ABC):                       # inherits from ABC

    @abstractmethod
    def area(self):                     # subclasses MUST implement this
        pass

    @abstractmethod
    def perimeter(self):                # subclasses MUST implement this
        pass

    def describe(self):                 # regular method — NOT abstract
        return f"Area: {self.area():.2f}  Perimeter: {self.perimeter():.2f}"


# ── Subclass that implements all abstract methods ──────

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):                     # implements abstract method
        return self.width * self.height

    def perimeter(self):                # implements abstract method
        return 2 * (self.width + self.height)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):                     # implements abstract method
        return 3.14159 * self.radius ** 2

    def perimeter(self):                # implements abstract method
        return 2 * 3.14159 * self.radius


# ── Using the subclasses ───────────────────────────────

rect = Rectangle(5, 3)
print(rect.describe())              # Area: 15.00  Perimeter: 16.00

circ = Circle(7)
print(circ.describe())              # Area: 153.94  Perimeter: 43.98

# ── Trying to instantiate the abstract class directly ──

# shape = Shape()                   # TypeError — cannot instantiate abstract class


# ── Subclass that forgets to implement a method ────────

class Triangle(Shape):

    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):                     # implements area
        return 0.5 * self.base * self.height

    # perimeter() not implemented

# t = Triangle(5, 3)                # TypeError — perimeter() not implemented