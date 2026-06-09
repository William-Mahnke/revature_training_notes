class Person:
    def __init__(self, name, age, ssn):
        self.name = name    # public - accessible everywhere
        self._age = age     # protected - accessible in subclasses
        self.__ssn = ssn    # private - only accessible in this class* (actually stored as '_ClassName__attributeName')
    
    def display_name(self):
        print(self.name)

    def display_ssn(self):
        print("ssn: ", self.__ssn)


class SubPerson(Person):
    def show_age(self):
        print("My Age: ", self._age)


person = Person("Person", 20, "123-45-6789")
print(person.name)
print(person._age) # We should not try to access this - follow conventions!
# print(person.__ssn) # Error - as expected
print (person._Person__ssn) # But actually...we can still access via the 'mangled name'

sub = SubPerson("Sub-Person", 10, "987-65-4321")
sub.show_age()