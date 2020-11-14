"""
In previous homework task 4,
you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'

"""
from collections import Callable


def cache(func: Callable, times=0) -> Callable:
    """Caches the function.

    Args:
        func: A function that needs to be cached.
        times: The number of times to return the cached value.

    Returns:
        Callable.

    """
    used_parameters = {}
    restart = times
    times = [times]
    parameters = [None]

    def cache_func(*args, **kwargs):
        if times[0] == restart or times[0] == -1:
            parameters.pop()
            times[0] = restart

            all_of_the_parameters = args + tuple(kwargs.keys()) + tuple(kwargs.values())
            if all_of_the_parameters not in used_parameters:
                used_parameters[all_of_the_parameters] = func(*args, **kwargs)

            parameters.append(all_of_the_parameters)
            times[0] -= 1

            return used_parameters[all_of_the_parameters]
        elif times[0] >= 0:
            times[0] -= 1

            return used_parameters[parameters[0]]

    return cache_func
