import datetime
from collections import defaultdict


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


class Person: # classes student and teacher are inherited from class person
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class DeadlineError(Exception):
    pass


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        else:
            raise DeadlineError("You are late.")


# accepts a Homework Result instance and returns True if the student's response is greater than 5 characters.
# On successful verification, add to homework_done

class Teacher(Person):
    homework_done = defaultdict()

    def create_homework(self, text: str, deadline: datetime.timedelta):
        Hw = Homework(text, deadline)
        return Hw

    def check_homework(self, HomeworkResult):
        if len(HomeworkResult.solution) > 5:
            self.homework_done[HomeworkResult.homework] = HomeworkResult.solution
            return True
        else:
            return False

    def reset_results(self, homework: Homework = None):
        if homework is not None:
            Teacher.homework_done[homework.text] = None
        else:
            Teacher.homework_done.clear()

# if you pass a Homework instance to the method, it only deletes the results of this task from homework_done
# if nothing is passed, it will completely reset homework_done.