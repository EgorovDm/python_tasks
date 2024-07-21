#!/usr/bin/env python3
import traceback

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
def string_to_ascii_dict(in_string: str) -> dict:
    ascii_dict_code = "{"
    for c in in_string:
        ascii_dict_code += f"    '{c}': '{c}'.encode(encoding='ascii').hex(),\n"
    ascii_dict_code = ascii_dict_code[:-2] + "}"
    return eval(ascii_dict_code)

print('='*20, 'DICTS', '='*20, sep='\n')
my_dict = string_to_ascii_dict(chars)
print(f'Defined dict:\n{my_dict}\n')
my_dict.update(string_to_ascii_dict('+-'))
print(f"Poping a:{my_dict['a']}\n")
my_dict.pop('a')
print(f"Poping b:{my_dict['b']}\n")
my_dict.pop('b')
print(my_dict)

print("Trying to access non existing key: ")

try:
    my_dict['b']
except:
    traceback.print_exc()

print('='*20, 'SETS', '='*20, sep='\n')
my_set = {1, "1", True}
print(my_set)
for element in [30, None]: my_set.add(element)
my_set.remove(1)
print(my_set)
