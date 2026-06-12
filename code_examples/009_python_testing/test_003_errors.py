# ═══════════════════════════════════════════════════════
# Testing Exceptions
# ═══════════════════════════════════════════════════════
# A well-written function not only behaves correctly under
# ideal conditions — it also handles invalid input and edge
# cases gracefully by raising appropriate exceptions.
#
# Testing that exceptions are raised correctly is just as
# important as testing the happy path.
#
# Key assertion methods for exception testing:
#   assertRaises(ExcType, callable, *args)
#       — passes if the callable raises ExcType when called with *args
#   assertRaisesRegex(ExcType, pattern, callable, *args)
#       — passes if the callable raises ExcType AND the exception
#         message matches the given regex pattern
#
# Both can also be used as context managers:
#   with self.assertRaises(ExcType):
#       some_function()
# ═══════════════════════════════════════════════════════
import unittest

# A custom exception class — inherits from the built-in Exception base class.
# Custom exceptions allow you to raise and catch specific, named error types
# that are meaningful in your application's domain.
class MyCustomError(Exception):
    """Custom Exception - Used for Exception Testing Example"""
    pass

# Production function that always raises our custom exception.
# Used to demonstrate basic assertRaises testing.
def my_func():
    raise MyCustomError("My error was raised")

# Production function that raises our custom exception with different
# messages depending on the input. Used to demonstrate assertRaisesRegex —
# verifying not just the exception type, but the specific message content.
def my_conditional_func(b: bool):
    if b:
        raise MyCustomError("It was True")
    else:
        raise MyCustomError("It was False")

class TestingErrors(unittest.TestCase):

    def test_my_func(self):
        # assertRaises(ExceptionType, callable) — verifies that calling
        # my_func() raises MyCustomError. The test passes if the exception
        # is raised; it fails if no exception is raised or a different
        # exception type is raised.
        self.assertRaises(MyCustomError, my_func)

    def test_my_conditional_func(self):
        # assertRaisesRegex(ExceptionType, pattern, callable, *args)
        # Extends assertRaises by also checking that the exception message
        # matches the given string/regex pattern.
        #
        # First call: passes True → expects the message "It was True"
        # Second call: passes False → expects the message "It was False"
        #
        # This is useful when a function raises the same exception type for
        # multiple reasons and you need to confirm the specific error is correct.
        self.assertRaisesRegex(MyCustomError, "It was True", my_conditional_func, True)
        self.assertRaisesRegex(MyCustomError, "It was False", my_conditional_func, False)
