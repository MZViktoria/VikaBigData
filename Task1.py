import datetime


# self - Accesses an object of a class and assigns an attribute to the object.
class Homework:
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        return (datetime.datetime.today() - self.created).days < self.deadline


class HomeworkResult:
    def __init__(self, homework, solution, author):
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, Homework):
        if Homework.is_active():
            return Homework
        else:
            print("You are late.")
            return None


# the method takes a Homework object and returns it if the task is already overdue, it prints 'You are late' and returns None

class Teacher(Person):
    def create_homework(self, text: str, deadline: datetime.timedelta):
        Hw = Homework(text, deadline)
        return Hw
