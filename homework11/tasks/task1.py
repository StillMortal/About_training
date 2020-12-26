"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"

"""


class SimplifiedEnum(type):
    """Simulates the work enum.py.
    Attention: members must be passed through the __keys class attribute.

    Args:
        *args: Special child class data. Not transmitted directly.
        **kwargs: Special child class data. Not transmitted directly.

    Attributes:
        child_name_plus_child_keys_var: Contains the class name and class attribute.

    """

    def __new__(mcs, *args, **kwargs):
        child_dunder_dict = args[-1]
        mcs.child_name_plus_child_keys_var = "_" + args[0] + "__keys"
        atribute_names = args[-1][mcs.child_name_plus_child_keys_var]
        for atribute_name in atribute_names:
            child_dunder_dict[atribute_name] = atribute_name

        return super().__new__(mcs, *args, **kwargs)

    def __iter__(self):
        for value in self.__dict__[SimplifiedEnum.child_name_plus_child_keys_var]:
            yield value

    def __len__(self):
        return len(self.__dict__[SimplifiedEnum.child_name_plus_child_keys_var])
