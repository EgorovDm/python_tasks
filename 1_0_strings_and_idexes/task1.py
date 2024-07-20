#!/usr/bin/env python

test_str_list = [
    'Топинамбур',
    'Urban'
]

for t_string in test_str_list:
    print(
        '='*15,
        f'Current string: {t_string}',
        '-'*15,
        'RESULT:',
        t_string[0],
        t_string[-1],
        t_string[len(t_string)//2:],
        t_string[::-1],
        t_string[1::2],
        '='*15,
        sep='\n'
    )
