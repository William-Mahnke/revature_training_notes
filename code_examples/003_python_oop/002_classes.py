# Classes are created with the 'class' keyword
class Car:
    # top-level defined attributes are 'class' attributes
    wheels = 4
    # __init__ method defines the constructor for the class
    def __init__(self, make, model, year):
        # attributes defined within the constructor are instance attributes
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        return f"{self.year}, {self.make} : {self.model}"
    
print( "=== Initial Instances [No Modification] ===")

car1 = Car("Toyota", "Corolla", 2025)
car2 = Car("Ford", "Mustang", 2023)

print( car1.describe(), f"I have {car1.wheels} wheel(s)")
print( car2.describe(), f"I have {car2.wheels} wheel(s)")

print("car 1 dict:", car1.__dict__)
print("car 2 dict:", car2.__dict__)
print("Car class dict:", Car.__dict__)

print( "=== car1 object Modification ===")

car1.year = 2021
car1.wheels = 2 # This adds an attribute to car1 object DOES NOT modify the Car class attribute of the same name
print( car1.describe(), f"I have {car1.wheels} wheel(s)")
print( car2.describe(), f"I have {car2.wheels} wheel(s)")

print("car 1 dict:", car1.__dict__) # Notice the addition of 'wheels' in car1 dict
print("car 2 dict:", car2.__dict__)
print("Car class dict:", Car.__dict__)

print( "=== Car class Modification ===")
Car.year = 2026
Car.wheels = 10
print( car1.describe(), f"I have {car1.wheels} wheel(s)")
print( car2.describe(), f"I have {car2.wheels} wheel(s)")

print("car 1 dict:", car1.__dict__)
print("car 2 dict:", car2.__dict__)
print("Car class dict:", Car.__dict__)
print(f"car1 Wheels [shadowing Car class]: {car1.wheels} | Car wheels [accessed using car1]: {car1.__class__.wheels}")
