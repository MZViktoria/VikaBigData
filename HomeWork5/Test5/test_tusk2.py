from HomeWork5.Task2 import custom_sum
import pytest


@pytest.mark.parametrize("a, b, c, expected_result", [(4, 3, 6, 13),
                                                      ([1, 13], [8, 17], [20, 1, 11], [1, 13, 8, 17, 20, 1, 11]),
                                                      ('hello,', ' world', ')', 'hello, world)')])
def test_custom_sum(a, b, c, expected_result):
    assert custom_sum(a, b, c) == expected_result


def test_name_attribute():
    assert custom_sum.__name__ == 'custom_sum'


def test_doc_attribute():
    assert custom_sum.__doc__ == 'This function can sum any objects which have __add___'


def test_orig_func_attribute():
    assert str(custom_sum.__original_func.__name__) == 'custom_sum'

