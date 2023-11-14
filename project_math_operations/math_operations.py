# math_operations.py

# Type hints are used in the function definitions to indicate the expected types of the parameters and return value.
# For example, 'a: float' indicates that 'a' is expected to be a float. Similarly, '-> float' indicates that the function is expected to return a float.

# This module defines basic mathematical operations.


def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


# Additional functions for subtract, multiply, and divide follow a similar format.
# They take two floats as input and return a float as output.


def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the difference.

    Args:
        a (float): The number from which to subtract.
        b (float): The number to subtract.

    Returns:
        float: The difference between a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the product.

    Args:
        a (float): The first number to multiply.
        b (float): The second number to multiply.

    Returns:
        float: The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the quotient.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a divided by b. If b is zero, returns 'float('inf')'.

    Raises:
        ZeroDivisionError: If the divisor (b) is zero.
    """
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero!")
