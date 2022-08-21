from utils import write_path, generate_path
from time import sleep
import random


while True:
    path = generate_path(random.randint(10, 30))
    write_path(path)

    print(f"Path: {path}")
    sleep(3)