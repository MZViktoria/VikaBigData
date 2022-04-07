"""
Homework принимает на вход 2 атрибута: текст задания и количество дней
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

# self - Accesses an object of a class and assigns an attribute to the object.
class Homework:
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        today = datetime.datetime.now()
        data = self.created + self.deadline
        return today <= data


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, Homework):
        if Homework.is_active():
            return Homework
        else:
            print("You are late.")
            return None


# the method takes a Homework object and returns it if the task is already overdue, it prints 'You are late' and returns None

class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, deadline: datetime.timedelta):
        Hw = Homework(f"{text}, {deadline}")
        return Hw


"""
h = Homework('home', datetime.timedelta(5))
print(h.is_active())

h.created -= datetime.timedelta(10)
print(h.created)
print(h.is_active())
"""
