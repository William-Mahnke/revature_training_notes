import sys

# Automatic interning of identifier-like strings
a = "hello"
b = "hello"

print("a == b | ", a == b)  # True, same value
print("a is b | ", a is b)  # Likely True, typically interned by python
print("id(a) | ", id(a))
print("id(b) | ", id(b))    # Same id — same object

# Strings that are calculated during runtime are (typically) NOT automatically interned
x = "hello world!!"
y = a + " world!!"

print("x == y | ", x == y)  # Truem, same value
print("x is y | ", x is y)  # False (usually), different objects in memory

x = sys.intern(x)
y = sys.intern(y)
print("=== After Intern ===")
print("x == y | ", x == y)  # True, still the same value
print("x is y | ", x is y)  # True - Now the same object in memory