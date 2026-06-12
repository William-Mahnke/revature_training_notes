# ═══════════════════════════════════════════════════════
# MagicMock
# ═══════════════════════════════════════════════════════
# MagicMock is a subclass of Mock that additionally supports
# Python's magic methods (dunder methods — __len__, __str__,
# __iter__, __enter__, __exit__, __getitem__, and more).
#
# A plain Mock will fail if the code under test uses the mock
# in a context that relies on magic methods — for example,
# calling len(), using it in a 'with' block, or iterating over
# it. MagicMock pre-configures these methods automatically.
#
# When to use MagicMock over Mock:
#   - The mock is used as a context manager (with ... as ...)
#   - The mock is passed to len(), iter(), str(), etc.
#   - The mock is accessed with square bracket notation obj["key"]
#   - As a general default when mocking real-world objects
# ═══════════════════════════════════════════════════════
import unittest
from unittest.mock import MagicMock

class TestMagicMock(unittest.TestCase):

    def test_magic_mock_len(self):
        # MagicMock pre-configures __len__ so that len() can be called on it.
        # A plain Mock() would raise a TypeError here because __len__ is not
        # set up by default.
        #
        # magic.__len__.return_value = 5 configures the magic method directly —
        # when len(magic) is called, Python invokes __len__ under the hood,
        # which returns 5.
        magic = MagicMock()
        magic.__len__.return_value = 5
        self.assertEqual(len(magic), 5)

    def test_magicmock_as_context_manager(self):
        # MagicMock supports __enter__ and __exit__ automatically — these are
        # the magic methods Python calls when entering and exiting a 'with' block.
        #
        # A plain Mock() would raise an AttributeError here because __enter__
        # and __exit__ are not set up by default.
        #
        # magic.__enter__.return_value configures what the 'with' block receives
        # as the 'ctx' variable — i.e. what is bound by 'as ctx'.
        magic = MagicMock()
        magic.__enter__.return_value = {"data":"value"}

        # Python calls magic.__enter__() on entry — ctx receives {"data": "value"}
        # Python calls magic.__exit__() on exit — even if an exception is raised
        with magic as ctx:
            self.assertEqual(ctx["data"], "value")

        # After the 'with' block, we can verify that both magic methods were
        # called exactly once — confirming the context manager protocol was
        # correctly exercised by the code under test.
        magic.__enter__.assert_called_once()
        magic.__exit__.assert_called_once()
