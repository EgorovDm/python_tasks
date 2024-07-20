#!/usr/bin/env python
# 3rd program

a = 1234
b = 5678

def middle_digits(digits: int) -> list:
    '''Retuns digigits in the middle'''
    return int(str(digits)[1:-1])

print(sum(list(map(middle_digits, [a, b]))))
