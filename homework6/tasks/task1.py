"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования

"""
import functools


def instances_counter(cls):
    """A decorator that is applied to a class and adds two new methods to it:
    - get_created_instances
    - reset_instances_counter

    Args:
        cls: Reference to the class.

    Returns:
        A reference to a class with two new methods.

    """

    def decorator_new_method(func):
        @functools.wraps(func)
        def wrapper_new_method(cls_par, *args, **kwargs):
            get_created_instances(1)
            return func(cls_par, *args, **kwargs)

        return wrapper_new_method

    cls.__new__ = decorator_new_method(cls.__new__)

    def get_created_instances(*args, counter=[0], **kwargs):
        if args and args[0] == 1:
            counter[0] += 1
        elif args and args[0] == 0:
            counter[0] = 0
        return counter[0]

    setattr(cls, "get_created_instances", get_created_instances)

    def reset_instances_counter(*args, **kwargs):
        instances_have_already_been_created = cls.get_created_instances()
        cls.get_created_instances(0)
        return instances_have_already_been_created

    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
