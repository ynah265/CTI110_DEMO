from unittest.mock import patch
import pytest
from print_operations import print_operations
from typing import Any

# Ensures the correct handling of outputs and their print representations.


@pytest.fixture(params=[(5.0, 3.0), (5, 0)])
def test_params(request: pytest.FixtureRequest):
    """
    Pytest fixture to supply pairs of numbers for testing the print operations.

    Args:
        request (pytest.FixtureRequest): A built-in pytest fixture providing information of the requesting test function.

    Returns:
        tuple: A pair of numbers (floats or integers) used as operands in the print operations tests.
    """
    return request.param


# The @patch decorator from the unittest module is used for mocking.
# It replaces the specified function with a mock object during the test execution.


# Mocking the 'add' function from the 'print_operations' module.
# Instead of executing the real 'add' function, any call to it during this test
# will return the string "add_result". This isolates the test from the actual
# implementation of the 'add' function and allows us to test how 'print_operations'
# handles this mocked return value.
@patch("print_operations.add", return_value="add_result")

# Similar to the previous line, this mocks the 'subtract' function in the
# 'print_operations' module. During the test, calling 'subtract' will
# simply return "subtract_result". This mock is useful to test the
# behavior of 'print_operations' when handling the output of 'subtract',
# independent of its actual subtracting logic.
@patch("print_operations.subtract", return_value="subtract_result")

# This line mocks the 'multiply' function. During the test, any call
# to 'multiply' will not perform its real operation but will return
# "multiply_result" instead. This allows testing of the 'print_operations'
# module's response to the mocked 'multiply' output without relying on
# the real multiplication logic.
@patch("print_operations.multiply", return_value="multiply_result")

# Mocking the 'divide' function from 'print_operations'. In this test,
# 'divide' will return "divide_result" irrespective of the input parameters.
# This is particularly helpful for testing how 'print_operations' handles
# the divide operation's output, for example, in scenarios like division by zero,
# where the actual function might have different behavior (like raising an exception).
@patch("print_operations.divide", return_value="divide_result")
def test_print_operations(
    mock_divide,
    mock_multiply,
    mock_subtract,
    mock_add,
    capsys: pytest.CaptureFixture[str],
    test_params: Any,
):
    """
    Test the print operations with mocked arithmetic operations.

    This function uses mocking to simulate the results of arithmetic operations and tests if the `print_operations` function correctly handles these results.

    Args:
        mock_divide, mock_multiply, mock_subtract, mock_add: Mocked functions for the arithmetic operations.
        capsys (pytest.CaptureFixture[str]): Fixture to capture stdout and stderr.
        test_params (Any): Parameters for the arithmetic operations, provided by the `test_params` fixture.

    Asserts:
        The correct handling of arithmetic operations and their print outputs by the `print_operations` function.
    """
    # Set the return values of the mock objects
    mock_add.return_value = "add_result"
    mock_subtract.return_value = "subtract_result"
    mock_multiply.return_value = "multiply_result"
    mock_divide.return_value = (
        "divide_result" if test_params[1] != 0 else "Cannot divide by zero!"
    )

    print_operations(*test_params)
    captured = capsys.readouterr()

    # Split the output into lines
    output = captured.out.strip().split("\n")

    # Check that the output is as expected
    assert (
        output[0] == f"The sum of {test_params[0]} and {test_params[1]} is add_result"
    )
    assert (
        output[1]
        == f"The difference between {test_params[0]} and {test_params[1]} is subtract_result"
    )
    assert (
        output[2]
        == f"The product of {test_params[0]} and {test_params[1]} is multiply_result"
    )
    if test_params[1] != 0:
        assert (
            output[3]
            == f"The division of {test_params[0]} by {test_params[1]} results in divide_result"
        )
    else:
        assert "Cannot divide by zero!" in output[3]
