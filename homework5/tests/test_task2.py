from homework5.tasks.task2 import print_result


def sum_of_only_three_parameters(a, b, c, *args):
    """Finds the sum of only three parameters.

    Args:
        a: The first element of the sum.
        b: The second element of the sum.
        c: The third element of the sum.
        *args: All else.

    Returns:
        The sum of only three parameters.

    """
    return a + b + c


def test_decorated_func_prints_correct_value(capsys):
    decorated_func = print_result(sum_of_only_three_parameters)
    decorated_func(1, 2, 3, 4)
    captured = capsys.readouterr()

    assert captured.out == "6\n"


def test_decorated_func_returns_correct_value():
    decorated_func = print_result(sum_of_only_three_parameters)
    returned_value = decorated_func(1, 2, 3, 4)

    assert returned_value == 6


def test_decorated_func_has_its_own_doc():
    decorated_func = print_result(sum_of_only_three_parameters)
    decorated_func(1, 2, 3, 4)

    assert decorated_func.__doc__ == sum_of_only_three_parameters.__doc__


def test_decorated_func_has_its_own_name():
    decorated_func = print_result(sum_of_only_three_parameters)
    decorated_func(1, 2, 3, 4)

    assert decorated_func.__name__ == sum_of_only_three_parameters.__name__


def test_decorated_func_has_original_func_attribute():
    decorated_func = print_result(sum_of_only_three_parameters)
    decorated_func(1, 2, 3, 4)

    assert decorated_func.__original_func == sum_of_only_three_parameters
