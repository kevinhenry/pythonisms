from functools import wraps
# from time import sleep

def counter(fuction):
    @wraps (function)
    def added_info(*args, **kwargs):
        base = fuction(*args, **kwargs)
        number = base.count('\n')
        return f'{base}\n========\n{number} line entries\n=====\n'
    return added_info

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
#     print(just_saying("I love star wars!"))
    # sith1 = "Darth Revan"
    # sith2 = "Darth Vader"
    # sith3 = "Darth Bane"

    # def sith_args(*args):
    #     for sith in args:
    #         print(f"{sith} is a Dark Lord of the Sith!")

    # def sith_kwargs(*kwargs):
    #     for item, sith in kwargs.items():
    #         print(item, sith)

    # sith_kargs(sith1 = 'Darth Revan', sith2 = 'Darth Vader', sith3 = 'Darth Bane')

    # sith_args(sith_kwargs)
