import random
import string


def generate_path(length) -> str:
    source = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(source) for i in range(length))
    
    return result_str


def read_path() -> str:
    with open("path.txt", "r") as file:
        path = file.readline()
        return path


def write_path(path: str) -> None:
    with open("path.txt", "w") as file:
        file.write(path)

