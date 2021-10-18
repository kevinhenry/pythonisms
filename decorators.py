from functools import wraps, cache, lru_cache
from time import sleep

# saves to memory but limits to last 5
@lru_cache(maxsize=5)
# a function which computes the nth fibonacci number and it does so in a recursive fashin - from mCoding
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# loop going through 400 numbers and printing out their fibonacci numbers
def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


if __name__ == "__main__":
    main()

# cache saves to memory
@cache
# a function which computes the nth fibonacci number and it does so in a recursive fashin - from mCoding
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")


if __name__ == "__main__":
    main()


# decorators basics from Kite
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper


@f1
def f(a, b=9):
    print(a, b)


@f1
def add(x, y):
    return x + y


print(add(4, 5))


# timer decorator - from kite
import time


def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")

    return wrapper


@timer
def run():
    time.sleep(2)


run()

# record everytime a function is run in a log - from kite
import datetime


def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at ")
        val = func(*args, **kwargs)
        return val

    return wrapper


@log
def run(a, b, c=9):
    print(a + b + c)


run(1, 3, c=9)


# def counter(fuction):
#     @wraps (function)
#     def added_info(*args, **kwargs):
#         base = fuction(*args, **kwargs)
#         number = base.count('\n')
#         return f'{base}\n========\n{number} line entries\n=====\n'
#     return added_info

# def yo_mamma_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         orig_val = func(*args, **kwargs)
#         return f'Yo mamma says "{orig_val}"'

#     return wrapper


# def sophisticated_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         orig_val = func(*args, **kwargs)
#         return f'Would you like some tea and crumpets as you say "{orig_val}"'

#     return wrapper


# @yo_mamma_decorator
# @sophisticated_decorator
# def just_saying(txt):
#     return txt


# if __name__ == "__main__":
#     print(just_saying("I love dogos!"))
# dogo1 = "Dogo Rey"
# dogo2 = "Dogo Starbuck"
# dogo3 = "Dogo Vesper"

# def dogos_args(*args):
#     for dogos in args:
#         print(f"{dogos} is an Awesome Dogo!")

# def dogos_kwargs(*kwargs):
#     for item, dogos in kwargs.items():
#         print(item, dogos)

# dogos_kargs(dogos1 = 'Dogo Rey', dogos2 = 'Dog Starbuck', dogos3 = 'Dogo Vesper')

# dogos_args(dogos_kwargs)
