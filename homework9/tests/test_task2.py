from homework9.tasks.task2 import ContextManager, managed_exception


def test_the_class_suppresses_the_exception():
    with ContextManager(IndexError):
        [][2]

    assert True


def test_the_class_suppresses_the_exception2():
    with ContextManager(ValueError):
        int("char")
        [][2]

    assert True


def test_the_generator_suppresses_the_exception():
    with managed_exception(IndexError):
        [][2]

    assert True


def test_the_generator_suppresses_the_exception2():
    with managed_exception(ValueError):
        int("char")
        [][2]

    assert True
