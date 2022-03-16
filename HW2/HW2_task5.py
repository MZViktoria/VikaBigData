"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import Any
#
def custom_range(mis: str, *args: Any):
    if len(args) == 1:
        index = mis.index(args[0])
        return mis[:index]
    elif len(args) == 2:
        start_index = mis.index(args[0])
        end_index = mis.index(args[1])
        return mis[start_index:end_index]
    elif len(args) > 2:
        start_index = mis.index(args[0])
        end_index = mis.index(args[1])
        return mis[start_index:end_index:args[2]]
    else:
        return mis

"""
If we have 1 argument, we return values up to this argument. 
If we have 2 arguments, we take the range from 1 to 2 arguments, taking into account the step.
"""
print(custom_range("abcdef", "d", "a", -2))
