"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2
"""
from collections.abc import Callable
from functools import lru_cache


def cache(func: Callable) -> Callable:

    @lru_cache # We use a decorator to pass another function as an argument.
    def inner(*args):
        return func(*args)

    return inner


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 2, 4

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

print(val_1)
