#!/usr/bin/env python3
calls = 0

def count_calls(func):
    def wrapper(*args, **kwords):
        global calls
        calls += 1
        return func(*args, **kwords)
    return wrapper

@count_calls
def string_info(in_str: str) -> tuple:
    '''принимает аргумент - строку и возвращает кортеж из: длины этой строки,
      строку в верхнем регистре, строку в нижнем регистре'''
    return (
        len(in_str),
        in_str.upper(),
        in_str.lower()
    )

@count_calls
def is_contains(in_str: str, ref_list: list) -> bool:
    '''принимает два аргумента: строку и список, и возвращает True,
      если строка находится в этом списке, False - если отсутствует. 
      Регистром строки при проверке пренебригает'''
    return in_str.upper() in [s.upper() for s in ref_list]


# Test code
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
