import time
from typing import Callable


def hello():
    print('world')


def prikol(func: Callable) -> None:
    print('hi')
    def inner(*args):
        func(*args)
    print('by')


print(time.time())
print()