# main.py

# Import the module that contains functions for printing operations
import print_operations
from input_validation import get_validated_float_input

# Allows the user to re-enter only the invalid number.
# The other number is kept as is.

# Separate functions for getting user input for each number, especially if you
# anticipate the need to handle more inputs in the future (e.g. a third number).
# or if you want to add specific validation or processing for each input.
# This approach increases modularity and reusability of your code.

# Each function can be tailored for specific input requirements, making the code more maintainable and easier to update or extend.


def get_user_input():
    """
    Prompts the user to enter two numbers and returns them as a tuple.

    Returns:
        tuple of float: A tuple containing two float numbers entered by the user.
    """
    a = get_validated_float_input("Enter the first number: ")
    b = get_validated_float_input("Enter the second number: ")
    return a, b


# The main function of the script, which performs operations using the user's input.
def main(a, b):
    """
    The main function of the script, performing print operations on given numbers.

    Args:
        a (float): The first number.
        b (float): The second number.
    """
    print_operations.print_operations(a, b)


if __name__ == "__main__":
    # Entry point of the script. Gets user input and calls the main function.
    # This last part of the script checks if this script is being run directly or being imported as a module.
    # If it's being run directly, it calls the main function. This is a common Python idiom to prevent
    # code from being run when the module is imported.
    a, b = get_user_input()
    main(a, b)
