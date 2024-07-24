#!/usr/bin/env python3

def get_multiplied_digits(in_num: int) -> int:
    '''Recurcive digit multiplication function'''
    if not type(in_num) == int:
        raise ValueError('Only integers are supported!')
    in_num = str(in_num)
    return int(in_num[0]) * (
        get_multiplied_digits(int(in_num[1:])) if len(in_num) > 1 else 1
    )

print(
    get_multiplied_digits(40203)
)
