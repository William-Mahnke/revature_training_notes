# ═══════════════════════════════════════════════════════
# Patch
# ═══════════════════════════════════════════════════════
# 'patch' temporarily replaces an object in a module's
# namespace with a mock for the duration of a test, then
# restores the original automatically when the test ends.
#
# This allows you to mock out a dependency (such as an
# external HTTP call) without modifying the production code.
#
# patch can be used in two ways:
#   1. As a context manager: 'with patch("target") as mock:'
#      The patch is active only within the 'with' block.
#
#   2. As a decorator: '@patch("target")'
#      The patch is active for the entire test method.
#      The mock is automatically passed as an extra argument.
#
# Critical rule — patch the object WHERE IT IS USED, not
# where it is defined. Here, requests.get is used directly
# via the 'requests' module, so we patch "requests.get".
# If the code had done 'from requests import get', we would
# need to patch the name in THAT module instead.
# ═══════════════════════════════════════════════════════
import unittest
from unittest.mock import Mock, patch
import requests

# "Production code" getting tested
# get_temperature() makes a real HTTP call to an external API.
# In tests, we patch requests.get to prevent the real call
# and return controlled data instead.
def get_temperature(city):
    response = requests.get(f"https://api.weather.com/{city}")
    data = response.json()
    return data["temperature"]

# Tests
class TestPatching(unittest.TestCase):

    def test_get_temperature_context_manager(self):
        # patch() used as a context manager — 'with patch(...) as mock_get:'
        # For the duration of this block, requests.get is replaced with mock_get.
        # When the block exits, requests.get is automatically restored.
        with patch("requests.get") as mock_get:

            # Create a mock response object to represent what requests.get would return.
            # Mock() is used here (rather than MagicMock) because .json() is a regular
            # method call — no magic methods are needed.
            mock_response = Mock()
            mock_response.json.return_value = {"temperature": 23}

            # Tell mock_get to return our fake response when called.
            # This means requests.get(url) → mock_response → mock_response.json() → {"temperature": 23}
            mock_get.return_value = mock_response

            result = get_temperature("London")

            # Assert the return value — verifying the function correctly extracts
            # the temperature from the response dictionary.
            self.assertEqual(result, 23)

            # Assert behaviour — verifying requests.get was called with the correct URL.
            # This confirms the function constructs the URL properly.
            mock_get.assert_called_once_with("https://api.weather.com/London")

# Note: test_get_temperature_decorator is defined outside the class below.
# This is a structural bug in the file — it should be indented inside
# TestPatching to be discovered and run by unittest. As written, it is
# a standalone function and will not be executed by the test runner.

@patch("requests.get")
def test_get_temperature_decorator(self, mock_get):
    # @patch() used as a decorator — the patch is active for the entire
    # test method. The mock is automatically passed as the last argument
    # (mock_get), after 'self'.
    #
    # When stacking multiple @patch decorators, they are applied bottom-up —
    # the bottommost decorator's mock is the first extra argument.
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 19}
    mock_get.return_value = mock_response

    result = get_temperature("Paris")
    self.assertEqual(result, 19)
    mock_get.assert_called_once_with("https://api.weather.com/Paris")
