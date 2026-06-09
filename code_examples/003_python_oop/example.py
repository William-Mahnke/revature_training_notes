# Used with 'encap.py' to showcase encapsulation
from encap import Person
from encap import SubPerson


p = Person("Joseph", 30, 123-45-6789)

print(p.name)
print(p._age)

s = SubPerson("Sub", 30, 123-45-6789)
print(s.name)
print(s._age)
