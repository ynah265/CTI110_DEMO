# print_operations.py
# This module uses functions from math_operations to perform and print the results.

# Import math operations from the same source directory
from math_operations import add, subtract, multiply, divide


def print_operations(a: float, b: float) -> None:
    """
    Prints the results of various mathematical operations on two numbers.

    This function uses the math_operations module to perform basic arithmetic
    operations (addition, subtraction, multiplication, and division) on two
    numbers and then prints the results.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        None
    """
    # Printing the sum of a and b
    print(f"The sum of {a} and {b} is {add(a, b)}")

    # Printing the difference between a and b
    print(f"The difference between {a} and {b} is {subtract(a, b)}")

    # Printing the product of a and b
    print(f"The product of {a} and {b} is {multiply(a, b)}")

    # Printing the division result of a by b. If b is zero, it prints an error message from the divide function.
    try:
        print(f"The division of {a} by {b} results in {divide(a, b)}")
    except ZeroDivisionError as e:
        print(e)
