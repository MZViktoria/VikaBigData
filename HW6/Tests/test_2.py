import pytest
import HW6.Task2 as task2

user = task2.User()


def test_classname():
    assert user.__class__.__name__ == 'Counter'


def test_instances():
    assert user.counter == 1


def test_instances_up():
    _, _ = task2.User(), task2.User()
    assert user.counter == 3


def test_instances_reset():
    user.reset_instances_counter()
    assert user.counter == 0