# ═══════════════════════════════════════════════════════
# Mocking
# ═══════════════════════════════════════════════════════
# Mocking is the practice of replacing real dependencies
# with controlled, fake substitutes during testing.
#
# A mock object records every interaction made with it —
# you can configure it to return specific values, and after
# the test you can inspect it to verify it was called in
# the expected way (correct arguments, correct number of times).
#
# This allows tests to be fast, repeatable, and independent
# of external systems (databases, APIs, file systems).
#
# Key tools from unittest.mock used here:
#   Mock()             — creates a mock object
#   return_value       — configures what the mock returns when called
#   assert_called_once() — asserts the mock was called exactly once
#   assert_called_once_with() - asserts the mock was called exactly once
#                                with the arguments provided
#   call_count         — the number of times the mock was called
#   call_args_list     — a list of 'call' objects recording every call made
# ═══════════════════════════════════════════════════════
import unittest
from unittest.mock import Mock

class TestMockOverview(unittest.TestCase):

    def setUp(self):
        # Create a basic mock object and configure its return value.
        # setUp() runs before each test, so each test receives a fresh
        # mock with a clean call history — preventing call counts from
        # carrying over between tests.
        self.mock_service = Mock()
        self.mock_service.get_user.return_value = {"id": 1, "name":"Agatha"}

    # Admittedly - not very useful test
    def test_mock_returns_configured_value(self):
        # Verifies that calling get_user() returns the value we configured
        # via return_value. This confirms our mock is wired up correctly
        # before relying on it in more meaningful tests.
        result = self.mock_service.get_user(1)
        self.assertEqual(result, {"id": 1, "name":"Agatha"})

    def test_mock_was_called(self):
        # assert_called_once() — verifies the mock was called exactly once.
        # This tests behaviour: not just what was returned, but that the
        # method was actually invoked by the code under test.
        self.mock_service.get_user(1)
        self.mock_service.get_user.assert_called_once()

    def test_mock_last_call_count(self):
        # call_count — the total number of times the mock was called.
        # Because setUp() creates a fresh mock before each test, the
        # count here starts at 0 and reflects only this test's calls.
        self.mock_service.get_user(1)
        self.mock_service.get_user(2)
        self.assertEqual(self.mock_service.get_user.call_count,2)

    def test_mock_func(self):
        # Mock can also be used as a standalone callable (not just as a
        # method on a service). Passing return_value= at construction time
        # is shorthand for setting mock_func.return_value = 100.
        mock_func = Mock(return_value=100)
        self.assertEqual(mock_func(), 100)
        mock_func.assert_called_once()

    def test_mock_func_call_list(self):
        # call_args_list — an internal list maintained by unittest.mock
        # that records every call made to the mock.
        #
        # Each item in the list is a 'call' object — a special type that
        # stores the arguments from one individual call:
        #   call.args   — a tuple of the positional arguments
        #   call.kwargs — a dict of the keyword arguments
        #
        # For mock_func(1), the call object has:
        #   call.args == (1,)  |  call.kwargs == {}
        #
        # call.args[0] reaches into the tuple to extract the first
        # positional argument — in this case 1, 2, or 3 for each call.
        mock_func = Mock()
        mock_func(1)
        mock_func(2)
        mock_func(3)

        self.assertEqual(mock_func.call_count, 3)

        # the call_args_list is an internal list maintained by unittest.mock
        # each item of the list is a 'call' object, that contains a tuple of
        # arguments, and dict of kwargs
        # i.e. for mock_func(1), the call object would have: call.args == (1) | call.kwarg == {}
        # we can use that structure to access the actual args:
        # call.args (the tuple) - then reference an index

        # Note the following is equivalent to:
        # calls = [call.args[0] for call in mock_func.call_args_list]
        calls = []
        for call in mock_func.call_args_list:  # iterate over each recorded call
            first_argument = call.args[0]       # grab the first positional argument
            calls.append(first_argument)        # add it to the list
        self.assertEqual(calls, [1,2,3])
