# ═══════════════════════════════════════════════════════
# SKIPPING TESTS
# ═══════════════════════════════════════════════════════
# There are legitimate situations where a test cannot or
# should not run under certain conditions — for example,
# when a feature is not yet implemented, or when the test
# only applies to a specific operating system or Python version.
#
# unittest provides a set of skip decorators to handle these
# scenarios cleanly, rather than allowing tests to fail with
# misleading errors.
#
# Skip decorators:
#   @unittest.skip("reason")        — always skips the test
#   @unittest.skipIf(cond, "reason") — skips if condition is True
#   @unittest.skipUnless(cond, "reason") — skips if condition is False
#   @unittest.expectedFailure       — test is expected to fail
#
# Skipped tests appear as 's' in the test runner output.
# Expected failures appear as 'x'; unexpected passes as 'u'.
# ═══════════════════════════════════════════════════════
import unittest
import sys

class TestSkipping(unittest.TestCase):

    @unittest.skip("Feature not yet implemented")
    def test_skip_future_feature(self):
        # @unittest.skip — unconditionally skips this test every time.
        # Useful during development when a test is written before the
        # feature it covers has been implemented. Should not be left
        # in place indefinitely — a permanently skipped test provides no value.
        self.assertEqual(1+2, 3) # this never runs

    @unittest.skipIf(sys.platform == "win32", "Test des not run on Windows")
    def test_unix_file_path(self):
        # @unittest.skipIf(condition, reason) — skips the test when the
        # condition evaluates to True. Here, the test is skipped on Windows
        # because Unix-style file paths are not valid on that platform.
        # sys.platform returns the current operating system identifier.
        path = '/usr/local/bin'
        self.assertTrue(path.startswith('/'))

    @unittest.skipUnless(sys.version_info >= (3, 10), "Required Python 3.10 or later")
    def test_requires_python_310(self):
        # @unittest.skipUnless(condition, reason) — skips unless the condition
        # is True. The inverse of skipIf. Here, the test only runs on Python 3.10+
        # because the 'match' statement (structural pattern matching) was
        # introduced in that version.
        # sys.version_info provides the current Python version as a named tuple.
        value = 42
        match value:
            case 42:
                result = "found"
            case _:
                result = "not found"
        self.assertEqual(result, "found")

    @unittest.expectedFailure
    def test_known_bug(self):
        # @unittest.expectedFailure — marks a test that is known to fail,
        # typically because it documents a known bug not yet fixed.
        #
        # If the test fails as expected → reported as 'x' (expected failure) ✓
        # If the test unexpectedly passes → reported as 'u' (unexpected success)
        # An unexpected success signals the bug may have been fixed, and the
        # decorator should be removed.
        #
        # This test documents a known bug - it should fail now, but will pass later, when fixed
        self.assertTrue(self.broken_behavior())

    def broken_behavior():
        return False
