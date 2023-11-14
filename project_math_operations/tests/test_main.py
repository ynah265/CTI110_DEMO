# test_main.py

import pytest
from unittest import mock
from main import get_user_input

# In this test module, the unittest.mock.patch method is used to replace the built-in input function with a mock that returns predetermined values.
# This allows the test to simulate user input without actual user interaction, ensuring that the get_user_input function correctly converts the input
# strings to floats and returns them as a tuple. This approach is essential for testing user input functions in an automated and controlled manner

# Tests user input functionality in the main module.


def test_get_user_input():
    """
    Test the get_user_input function from the main module.

    This test ensures that the get_user_input function correctly processes user input:
    - Mocks the built-in input function to provide predetermined responses.
    - Tests with different sets of inputs to ensure correct parsing and type conversion.

    Asserts:
        The function returns a tuple of floats corresponding to the mocked inputs.
    """
    with mock.patch("builtins.input", side_effect=["5", "10"]):
        assert get_user_input() == (5.0, 10.0)

    with mock.patch("builtins.input", side_effect=["5.5", "10.5"]):
        assert get_user_input() == (5.5, 10.5)
