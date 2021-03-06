"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.

"""
import datetime
from typing import Union


class Homework:
    """Create a new Homework object from the given str object and int object.
    The text and deadline arguments are required.

    Args:
        text: A string representing the homework.
        deadline: Number of days to complete your homework.

    Attributes:
        text: A string representing the homework.
        deadline: Number of days to complete your homework.
        created: The time when the homework was created.

    """

    def __init__(self, text: str, deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Whether the time for completing your homework is up.

        Returns:
            True if successful, False otherwise.

        """
        return datetime.datetime.now() - self.created < self.deadline


class Student:
    """Create a new Student object from the given str object and str object.
    Given str object and str object are the student's last name and first name.

    Args:
        last_name: Last name of a student.
        first_name: First name of a student.

    Attributes:
        last_name: Last name of a student.
        first_name: First name of a student.

    """

    def __init__(self, last_name: str = "", first_name: str = "") -> None:
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(hw: Homework) -> Union[Homework, None]:
        """Whether the time for completing your homework is up.

        Args:
            hw: Homework instance.

        Returns:
            Homework instance if successful, None otherwise.

        """
        if hw.is_active():
            return hw
        else:
            print("You are late.")
            return None


class Teacher:
    """Create a new Teacher object from the given str object and str object.
    Given str object and str object are the teacher's last name and first name.

    Args:
        last_name: Last name of a teacher.
        first_name: First name of a teacher.

    Attributes:
        last_name: Last name of a teacher.
        first_name: First name of a teacher.

    """

    def __init__(self, last_name: str = "", first_name: str = "") -> None:
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Creates a Homework instance.

        Args:
            text: A string representing the homework.
            deadline: Number of days to complete your homework.

        Returns:
            Homework instance.

        """
        return Homework(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
