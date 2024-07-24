#!/usr/bin/env python3
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def to_int(in_obj) -> int:
    '''converts string to int as length
    and other objects to int '''
    if type(in_obj) == str:
        return len(in_obj)
    else:
        return int(in_obj)

def to_list(in_obj) -> list:
    '''Convert dict to list, standart conversion strips values'''
    if type(in_obj) == dict:
        return list(in_obj.keys()) + list(in_obj.values())
    else:
        return list(in_obj)

def flatten_v1(in_struct) -> list:
    '''Flattening through string representation, quick and easy'''
    return eval(
        f'''[{str(in_struct).translate({ord(c): None for c in '[]{}()'}).replace(':',',').replace(', ,',',')}]'''
    )

def flatten_v2(in_struct: list) -> list:
    '''Flattening structure recursively, more complex way'''
    in_struct = to_list(in_struct)
    if in_struct == []:
        return []
    if not(type(in_struct[0]) in [list, dict, set, tuple]):
        return [in_struct[0]] + flatten_v2(in_struct[1:])
    else:
        return flatten_v2(in_struct[0]) + flatten_v2(in_struct[1:])

print(
    "1st way:",
    sum(list(map(to_int ,flatten_v1(data_structure)))),
    "2d way:",
    sum(list(map(to_int ,flatten_v2(data_structure)))),
    sep="\n")
