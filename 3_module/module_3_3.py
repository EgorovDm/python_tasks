#!/usr/bin/env python3

def print_params(a: int = 1, b: str = 'строка', c: bool = True) -> None:
    '''Print params'''
    print(a, b, c, sep="  ")

values_list = [2, 'нестрока', False ]
values_dict = {
    'a': 1,
    'b': 'нестрока',
    'c': False
}
values_list2 = values_list[:2]

print_params()
print_params(*values_list)
print_params(*values_list2, False)
print_params(**values_dict)
