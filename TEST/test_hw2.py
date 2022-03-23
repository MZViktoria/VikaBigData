import string

import HW2.HW2_task3 as task3
import HW2.HW2_task4 as task4
import HW2.HW2_task5 as task5

import random



N = 3
range_of_values = 10
A = []
B = []
C = []
for i in range(0, N):
    A.append(random.randint(-range_of_values, range_of_values))
    B.append(random.randint(-range_of_values, range_of_values))
    C.append(random.randint(-range_of_values, range_of_values))


def test_task3():
    result = task3.combinations(A, B, C)
    assert result != None, "Result is None"
    assert len(result) > 0, "Result isn't None, but it's empty"
    assert type(result) == list, "Result isn't list"


def test_task4():
    result = task4.cache_func(A[0], B[1])
    assert result != None, "Result is None"
    assert type(result) != str, "Result isn't a number"
    assert (A[0] ** B[1]) ** 2 == result, "Function doesn't work correctly"


text = string.ascii_lowercase
index_start = random.randint(0, len(text)-1)
index_end = random.randint(0, len(text)-1)
step = random.randint(1, len(text))


def test_task5():
    result = task5.custom_range(text, text[index_start], text[index_end], step)
    assert result != None, "Result is None"
    assert type(result) == str, "Result isn't a string"
    assert text[index_start:index_end:step] == result, "Function doesn't work correctly"