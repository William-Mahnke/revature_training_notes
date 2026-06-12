# ═══════════════════════════════════════════════════════
# WHAT ARE UNIT TESTS?
# ═══════════════════════════════════════════════════════
# A unit test verifies that a small, isolated piece of code
# behaves as expected. In Python, the 'unittest' module is
# the standard library's built-in testing framework.
#
# Tests are organised into classes that inherit from
# unittest.TestCase. Each test is a method on that class
# whose name begins with 'test_' — this is how the test
# runner discovers and executes them automatically.
#
# unittest provides a set of 'assertion methods' to validate
# outcomes. If an assertion fails, the test is marked as
# failed. If all assertions pass, the test passes.
# ═══════════════════════════════════════════════════════
import unittest

# TestCase is the base class all test classes must inherit from.
# It provides all assertion methods (assertEqual, assertTrue, etc.)
# and hooks for setup and teardown (setUp, tearDown).
class TestExamples(unittest.TestCase):

    def test_checking_equality(self):
        # assertEqual(a, b) — passes if a == b
        # Use this when you expect two values to be identical.
        a = 1
        b = 1
        self.assertEqual(a,b)

    def test_checking_not_equal(self):
        # assertNotEqual(a, b) — passes if a != b
        # Use this when you want to confirm two values are different.
        a = 1
        b = 2
        self.assertNotEqual(a,b)

    def test_checking_truthy(self):
        # assertTrue(x) — passes if x evaluates to True
        # Use this when checking a boolean condition or expression.
        self.assertTrue(10 > 5)

    def test_checking_falsy(self):
        # assertFalse(x) passes if x evaluates to False
        # Note: this test uses assertTrue — both demonstrate boolean assertion patterns
        self.assertFalse(10 < 5)

    def test_checking_collections(self):
        # assertIn(a, b) — passes if a is a member of b
        # Use this when verifying that a value exists within a list, set, or other iterable.
        a = 1
        b = [1,2,3,4]
        self.assertIn(a, b)
