import pytest
from print_operations import print_operations
from math_operations import add, subtract, multiply, divide
from typing import Any

# In this test module, the fixture test_params provides parameters for the test function test_print_operations,
# which asserts that the output of the print_operations function is as expected for each arithmetic operation.
# The use of the capsys fixture to capture the output is essential for verifying the print functionality
# Tests the output of the print_operations function for each arithmetic operation.


@pytest.fixture(params=[(5.0, 3.0), (5, 0)])
def test_params(request: pytest.FixtureRequest):
    """
    A pytest fixture that generates pairs of numbers for testing arithmetic operations.

    Args:
        request (FixtureRequest): A special built-in pytest fixture that provides information of the requesting test function.

    Returns:
        tuple: A pair of numbers, either floats or integers, to be used as operands in arithmetic operations.
    """
    return request.param


def test_print_operations(capsys: pytest.CaptureFixture[str], test_params: Any):
    """
    Test the print operations for various arithmetic functions.

    This function checks if the print output for addition, subtraction, multiplication, and division (if not by zero) is correctly implemented.

    Args:
        capsys (CaptureFixture): Pytest fixture to capture stdout and stderr.
        test_params (tuple): A tuple of two numbers, provided by the test_params fixture, used in the operations.

    Asserts:
        Correctness of the printed output for each arithmetic operation.
    """
    print_operations(*test_params)
    captured = capsys.readouterr()

    # Split the output into lines
    output = captured.out.strip().split("\n")

    # Check that the output is as expected
    assert (
        output[0]
        == f"The sum of {test_params[0]} and {test_params[1]} is {add(*test_params)}"
    )
    assert (
        output[1]
        == f"The difference between {test_params[0]} and {test_params[1]} is {subtract(*test_params)}"
    )
    assert (
        output[2]
        == f"The product of {test_params[0]} and {test_params[1]} is {multiply(*test_params)}"
    )
    if test_params[1] != 0:
        assert (
            output[3]
            == f"The division of {test_params[0]} by {test_params[1]} results in {divide(*test_params)}"
        )
    else:
        assert "Cannot divide by zero!" in output[3]
