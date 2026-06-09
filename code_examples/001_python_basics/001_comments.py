# Code comment
# Python does not support multi-line comments
def my_func():
    # doc strings (triple quotes) are used to document a module/class/function
    # doc strings should appear as the first line of the entity it is 
    """This showcases docstrings in functions"""
    pass
print(my_func.__doc__)

def add(a, b):
    """Returns the sum of two arguments, a and b"""
    return a + b
print(add.__doc__)

class Animal():
    # Docstrings can be multi-line
    """Represents an Animal Model

    Attributes:
        anim_id (int) : unique id for the animal
        anim_name (string) : full name of animal
    """
    def __init__(self, anim_id, anim_name):
        self.anim_id = anim_id
        self.anim_name = anim_name
print(Animal.__doc__)



def incorrect():
    print("docstrings should be placed in the first line of the method")
    """This Docstrings will not appear when referencings 'incorrect.__doc__"""
print(incorrect.__doc__) # None