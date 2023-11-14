import pytest
from print_operations import print_operations
from math_operations import add, subtract, multiply, divide

# This module's primary focus is on the print outputs of arithmetic operations.
# The tests ensure that the operations not only perform the correct calculations
# but also that their printed representations (such as "The sum of x and y is z") are accurate.
# The capsys fixture is crucial for capturing and asserting these print outputs.​​

# This test module contains unit tests for the math_operations module.


@pytest.fixture(params=[(5.0, 3.0), (5, 0)])
def test_params(request):
    """
    Pytest fixture to supply pairs of numbers for testing print operations.

    Args:
        request (FixtureRequest): A special built-in pytest fixture that provides information of the requesting test function.

    Returns:
        tuple: A pair of numbers (either floats or integers) to be used as operands in arithmetic operations.
    """
    return request.param


def test_print_operations(capsys, test_params):
    """
    Test the correctness of print outputs for various arithmetic operations.

    This function verifies if the print operations for addition, subtraction, multiplication, and division (excluding division by zero) are correctly implemented.

    Args:
        capsys (CaptureFixture): Pytest fixture to capture stdout and stderr.
        test_params (tuple): A tuple of two numbers provided by the test_params fixture for arithmetic operations.

    Asserts:
        The accuracy of the printed output for each arithmetic operation.
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
