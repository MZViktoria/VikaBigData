from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator[int]:
    m = []
    for i in file_list: # iterate over the addresses inside the array
        with open(i) as file: #Open the file at the given address
            for line in file: #We read each line in the file
                m.append(int(line[:len(line)-1])) #add a string to our array
    return iter(sorted(m)) #return sorted iterator
