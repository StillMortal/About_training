import pytest

from homework6.tasks.task1 import instances_counter


@pytest.fixture(scope="function")
def created_and_decorated_empty_class():
    @instances_counter
    class SomeClassName:
        pass

    return SomeClassName


def test_no_instances_exist(created_and_decorated_empty_class):

    assert created_and_decorated_empty_class.get_created_instances() == 0


def test_there_is_one_instance(created_and_decorated_empty_class):
    ins = created_and_decorated_empty_class()

    assert ins.get_created_instances() == 1


def test_there_are_two_instances(created_and_decorated_empty_class):
    created_and_decorated_empty_class()
    created_and_decorated_empty_class()

    assert created_and_decorated_empty_class.get_created_instances() == 2


def test_there_were_two_instances_and_they_were_deleted(
    created_and_decorated_empty_class,
):
    created_and_decorated_empty_class()
    created_and_decorated_empty_class()

    assert created_and_decorated_empty_class.reset_instances_counter() == 2


def test_the_counter_was_reset_to_zero(created_and_decorated_empty_class):
    created_and_decorated_empty_class()
    created_and_decorated_empty_class()
    created_and_decorated_empty_class.reset_instances_counter()

    assert created_and_decorated_empty_class.get_created_instances() == 0


@pytest.fixture(scope="function")
def created_and_decorated_class():
    @instances_counter
    class SomeClassName:
        def __init__(self, num):
            self.num = num

    return SomeClassName


def test_no_instances_exist2(created_and_decorated_class):

    assert created_and_decorated_class.get_created_instances() == 0


def test_there_is_one_instance2(created_and_decorated_class):
    ins = created_and_decorated_class(8)

    assert ins.get_created_instances() == 1


def test_there_are_two_instances2(created_and_decorated_class):
    created_and_decorated_class(8)
    created_and_decorated_class(9)

    assert created_and_decorated_class.get_created_instances() == 2


def test_there_were_two_instances_and_they_were_deleted2(created_and_decorated_class):
    created_and_decorated_class(8)
    created_and_decorated_class(9)

    assert created_and_decorated_class.reset_instances_counter() == 2


def test_the_counter_was_reset_to_zero2(created_and_decorated_class):
    created_and_decorated_class(8)
    created_and_decorated_class(9)
    created_and_decorated_class.reset_instances_counter()

    assert created_and_decorated_class.get_created_instances() == 0
