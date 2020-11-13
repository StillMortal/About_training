def check_power_of_2(a: int) -> bool:
    """Whether the number is a power of 2.

    Args:
        a: The number to check.

    Returns:
        True if successful, False otherwise.

    """
    return not (bool(a & (a - 1))) if a != 0 else False
