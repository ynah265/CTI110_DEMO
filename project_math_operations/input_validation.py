def validate_float(input_str):
    """
    Validates if the provided string can be converted to a float.

    Args:
        input_str (str): The string to be validated.

    Returns:
        tuple (bool, float or None): A tuple containing a boolean indicating if the input is valid,
        and the converted float or None if invalid.
    """
    try:
        return True, float(input_str)
    except ValueError:
        return False, None


def get_validated_float_input(prompt):
    """
    Repeatedly prompts the user for input until a valid float is entered.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        float: The validated float input from the user.
    """
    while True:
        user_input = input(prompt)
        is_valid, number = validate_float(user_input)
        if is_valid:
            return number
        print("Invalid input. Please enter a valid number.")
