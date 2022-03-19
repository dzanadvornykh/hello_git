import time
from typing import Callable


def hello():
    print('world')


def prikol(func: Callable) -> None:
    print('hi')
    def inner(*args):
        func(*args)
    print('by')


def foo(x: int) -> int:
    return x * 2


def bar(y: int) -> int:
    return y * y


print(time.time())
print()