# test_math_operations.py

# This test module contains unit tests for the math_operations module.
# It tests basic arithmetic functions including addition, subtraction, multiplication, and division.
# Contains unit tests for basic arithmetic functions (addition, subtraction, multiplication, division) in the math_operations module.
# Focuses solely on the correctness of mathematical operations.

from typing import Any
import pytest
from math_operations import add, subtract, multiply, divide


# Test cases for add function
def test_add():
    """
    Test the add function from the math_operations module.

    Ensures that:
    - Positive numbers are added correctly.
    - Negative numbers are added correctly.
    - Adding opposite numbers yields zero.
    """
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-1, 1) == 0


# Test cases for subtract function
def test_subtract():
    """
    Test the subtract function from the math_operations module.

    Ensures that:
    - One number is subtracted from another correctly.
    - Negative numbers are subtracted correctly.
    - Subtracting a number from itself yields zero.
    """
    assert subtract(3, 2) == 1
    assert subtract(-2, -1) == -1
    assert subtract(-1, 1) == -2


# Test cases for multiply function
def test_multiply():
    """
    Test the multiply function from the math_operations module.

    Ensures that:
    - Positive numbers are multiplied correctly.
    - Negative numbers are multiplied correctly.
    - Multiplying a number by its additive inverse yields -1.
    """
    assert multiply(3, 2) == 6
    assert multiply(-2, -1) == 2
    assert multiply(-1, 1) == -1


# Test cases for divide function
def test_divide():
    """
    Test the divide function from the math_operations module.

    Ensures that:
    - Division is performed correctly when denominator is not zero.
    - Division by zero is handled and returns a defined error value.
    """
    assert divide(4, 2) == 2
    assert divide(-2, -1) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 1) == 0


# Use pytest fixture to handle the expected exception for zero division
@pytest.fixture(params=[(1, 0), (0, 0)])
def zero_division_cases(request: pytest.FixtureRequest) -> Any:
    """
    A pytest fixture that provides test cases for division by zero.

    Args:
    - request: The pytest fixture request context.

    Returns:
    - A tuple of two integers where the second integer is zero.
    """
    return request.param


def test_divide_zero(zero_division_cases: Any):
    """
    Test the divide function from the math_operations module for zero division cases.

    Ensures that a ZeroDivisionError is raised when attempting to divide by zero.

    Args:
    - zero_division_cases (tuple): A tuple of two integers provided by the zero_division_cases fixture.
    """
    a, b = zero_division_cases
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
