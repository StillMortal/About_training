"""
We have a file that works as key-value storage,
each like is represented as key and value separated by = symbol,
example:
    name=kek
    last_name=top
    song_name=shadilay
    power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
    storage['name'] # will be string 'kek'
    storage.song_name # will be 'shadilay'
    storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.

"""
from string import ascii_letters, digits
from typing import Union


class KeyValueStorage:
    """Key-value storage class.

    Args:
        path_to_file: Path to file.

    Attributes:
        pairs: A dictionary containing a key and value pair.

    Raises:
        ValueError: if the key is not the correct attribute.


    """

    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file) as data:
            key_and_value = data.read().split()

        self.pairs = {}

        for pair in key_and_value:
            pair = pair.split("=")

            self.__setattr__(pair[0], pair[1])

    def __setattr__(self, key: str, value: Union[int, str]) -> None:
        """Adds a key-value pair to the dictionary.

        Args:
            key: Key to the dictionary.
            value: Value to the dictionary.

        """
        if self.__correct_attribute(key):
            try:
                self.__dict__[key] = int(value)
                self.__setitem__(key, int(value))
            except (ValueError, TypeError):
                self.__dict__[key] = value
                self.__setitem__(key, value)

    def __correct_attribute(self, attribute: str) -> Union[bool, None]:
        """Checks whether the received string object can be an attribute.

        Args:
            attribute: Possible attribute.

        Returns:
            True if successful.

        """
        if attribute[0] != "_" and attribute[0] not in ascii_letters:
            raise ValueError(f"the value {attribute} cannot be an attribute.")

        for char in attribute:
            if char != "_" and char not in ascii_letters and char not in digits:
                raise ValueError(f"the value {attribute} cannot be an attribute.")

        if attribute not in self.__dir__():
            return True

    def __getitem__(self, key: str) -> Union[int, str]:
        """Returns the value by key.

        Args:
            key: Key to the dictionary.

        Returns:
            Value.


        """
        return self.pairs[key]

    def __setitem__(self, key: str, value: Union[int, str]) -> None:
        """Sets the dictionary value by key.

        Args:
            key: Key to the dictionary.
            value: Value to the dictionary.

        """
        self.pairs[key] = value
