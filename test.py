import time


def hello():
    print('world')


def my_function(x: str, y: str) -> str:
    return x + y


def also_my_function(x: str) -> str:
    return f'hello, {x}'
print(time.time())
print()