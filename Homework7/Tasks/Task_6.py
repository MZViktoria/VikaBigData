import os
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    for file in dir_path.glob(f'*.{file_extension}'): #get a list of files in the specified directory
        with file.open('r') as f:
            if tokenizer is None:#check the presence of a tokinizer
                counter += len(f.readlines())
            else:
                counter += len(tokenizer(' '.join(f.readlines())))#we apply the function in our tokinizer and count the number of elements.
    return counter


print(universal_file_counter(Path('D:/BIGdata/Homework7/Tasks'), "txt", str.split))
