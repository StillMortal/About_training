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

    def __new__(mcs, name, bases, attr):

        # super_new = super().__new__(mcs, name, bases, attr)
        # mcs.child_name_plus_child_keys_var = "_" + super_new.__name__ + "__keys"
        # atribute_names = super_new.__dict__[mcs.child_name_plus_child_keys_var]
        # for atribute_name in atribute_names:
        #     super_new.__dict__[atribute_name] = atribute_name

        # return super_new

        child_dunder_dict = attr
        mcs.child_name_plus_child_keys_var = "_" + name + "__keys"
        atribute_names = attr[mcs.child_name_plus_child_keys_var]
        for atribute_name in atribute_names:
            child_dunder_dict[atribute_name] = atribute_name

        print(child_dunder_dict)

        return super().__new__(mcs, name, bases, attr)

    def __iter__(self):
        yield from self.__dict__[SimplifiedEnum.child_name_plus_child_keys_var]

    def __len__(self):
        return len(self.__dict__[SimplifiedEnum.child_name_plus_child_keys_var])
