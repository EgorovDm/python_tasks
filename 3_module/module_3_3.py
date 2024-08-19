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

print_params(10, 'строка', True)
print_params(a=30, b='нестрока', c=False)
print_params(c=True)
print_params(a=10, b='строка')
print_params(30, c=False)
print_params()
print_params(*values_list)
print_params(*values_list2, False)
print_params(**values_dict)
