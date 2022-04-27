"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    #return str(tree.values()).count(str(element))
    def counter(mnogestvo, elem):
        for val in (mnogestvo.values() if isinstance(mnogestvo,
                                                dict) else mnogestvo):  #we check the data type. is the element a dictionary or something else
            if val == elem:
                yield val
            elif isinstance(val, (list, tuple, set)):
                yield from counter(val, elem)
            elif isinstance(val, dict):
                yield from counter(val.values(), elem)
    return len(list(counter(tree, element)))


if __name__ == '__main__':
    print(example_tree.items())
    print(find_occurrences(example_tree, "RED"))  # 6
