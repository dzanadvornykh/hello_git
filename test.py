from math import factorial
import time
from typing import Callable


def hello():
    print('world')


def hi():
    print('dimon')


def my_func():
    print('kek')


def bobo():
    print('my bobo')


def prikol(func: Callable) -> Callable:
    print('hi')
    def inner(*args):
        func(*args)
    print('by')
    return inner


def foo(x: int) -> int:
    return x * 2


def bar(y: int) -> int:
    return y * y


def baz(z: int) -> int:
    return factorial(z)



def my_function(x: str, y: str) -> str:
    return x + y


def also_my_function(x: str) -> str:
    return f'hello, {x}'

  
print(time.time())
print()