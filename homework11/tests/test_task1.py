import pytest

from homework11.tasks.task1 import SimplifiedEnum


def test_class_with_only_keys():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert (ColorsEnum.XL, ColorsEnum.S, ColorsEnum.XS) == ("XL", "S", "XS")


def test_class_with_keys_and_init_method():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

        def __init__(self, value):
            self.value = value

    ins = ColorsEnum(7)

    assert ins.value == 7


def test_class_with_keys_and_init_method_but_doesnt_lose_basic_functionality():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

        def __init__(self, value):
            self.value = value

    ins = ColorsEnum(7)

    assert (ins.XL, ins.L, ins.M) == ("XL", "L", "M")


def test_class_with_keys_and_iteration_is_possible():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert [el for el in ColorsEnum] == ["XL", "L", "M", "S", "XS"]


def test_class_with_keys_and_length_search():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert len(ColorsEnum) == 5


def test_doesnt_work_with_inheritance():
    with pytest.raises(KeyError) as err:

        class ColorsEnum(metaclass=SimplifiedEnum):
            pass

        class ColorsEnum2(ColorsEnum):
            __keys = ("XL", "L", "M", "S", "XS")

    assert "_ColorsEnum__keys" in str(err.value)
