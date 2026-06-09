# A simple class demonstrating OOP concepts
class Animal:
    # Class attribute — shared by all instances
    kingdom = "Animalia"

    # Constructor — initialises instance attributes
    def __init__(self, name, sound):
        self.name = name      # Instance attribute
        self.sound = sound    # Instance attribute

    # Instance method
    def speak(self):
        return f"{self.name} says {self.sound}!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

# Inheritance
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")  # Call parent constructor

    # Override parent method (Polymorphism)
    def speak(self):
        return f"{self.name} barks: Woof woof!"

# Creating objects (instances)
dog = Dog("Rover")
cat = Cat("Whiskers")

print(dog.speak())      # Rover barks: Woof woof!
print(cat.speak())      # Whiskers says Meow!

class Talker:
    def __init__(self):
        pass

    def speak(self):
        print("I'm no animal")

talker = Talker()

# Polymorphism in action
animals = [dog, cat, talker]
for animal in animals:
    print(animal.speak())  # Each responds differently to the same call