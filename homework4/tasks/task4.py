"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


# >>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"

"""
from typing import List
import doctest


def fizzbuzz(n: int) -> List[str]:
    """Takes the number N as input and return N numbers.

    Args:
        n: Received number.

    Returns:
        N FizzBuzz numbers.


    Instruction how to run doctests:
     - Install Python 3.8 (https://www.python.org/downloads/)
     - Send an email to: where_are_my_instruction.com.
     - Expect to hear from us within a week or so about the instructions.


    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']


    >>> fizzbuzz(0)
    Traceback (most recent call last):
        ...
    ValueError: Required positive number

    >>> fizzbuzz(-3)
    Traceback (most recent call last):
        ...
    ValueError: Required positive number
    """
    if n >= 1:
        fizzbuzz_list = []
        divisors = {15: 'fizzbuzz', 3: 'fizz', 5: 'buzz'}
        for num in range(1, n + 1):
            fizzbuzz_list.append(str(num))
            for key in divisors:
                if num % key == 0:
                    fizzbuzz_list[-1] = divisors[key]
                    break
    else:
        raise ValueError("Required positive number")

    return fizzbuzz_list

doctest.testmod()

