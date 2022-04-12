import datetime
from HomeWork5.Task1 import Homework, Student, Teacher

expired_hw = Homework('calculate', -1)
actual_hw = Homework('read', 5)
student = Student('Roman', 'Petrov')
teacher = Teacher('Daniil', 'Ivanov')


class TestHomework:
    def test_hw_attributes(self):
        # testing HomeWork attributes
        assert expired_hw.text == 'calculate'
        assert actual_hw.deadline == 5

    def test_hw_is_active_method(self):
        # testing HomeWork attributes "is_active" method
        assert student.do_homework(expired_hw) is None
        assert student.do_homework(actual_hw) == actual_hw


class TestTeacher:
    def test_teacher_attributes(self):
        # testing Teacher attributes
        assert teacher.first_name == 'Daniil'
        assert teacher.last_name == 'Ivanov'

    def test_teacher_create_hw_method(self):
        # testing Teacher "create_hw" method
        assert teacher.create_homework("do something", 5).text == 'do something'


class TestStudent:
    def test_student_attributes(self):
        # testing Student attributes
        assert student.first_name == 'Roman'
        assert student.last_name == 'Petrov'

    def test_student_do_hw_method(self):
        assert student.do_homework(expired_hw) is None
        assert student.do_homework(actual_hw) is actual_hw
