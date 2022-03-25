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
"""
import datetime


class Homework:
    def __init__(self, text:str , deadline:datetime.timedelta ):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active (self):
        today=datetime.datetime.now()
        data= self.created+self.deadline
        return today<=data


h = Homework('home', datetime.timedelta(5))
print(h.is_active())

h.created -= datetime.timedelta(10)
print(h.created)
print(h.is_active())
