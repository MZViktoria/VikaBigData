from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        l = [int(line) for line in fi]
    return max(l), min(l)


print(find_maximum_and_minimum('number.txt'))
