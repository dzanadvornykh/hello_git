import time
from typing import Callable


def hello():
    print('world')


def prikol(func: Callable) -> Callable:
    print('hi')
    def inner(*args):
        func(*args)
    print('by')
    return inner

print(time.time())
print()