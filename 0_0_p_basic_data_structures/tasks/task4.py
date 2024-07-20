#!/usr/bin/env python
# 4th program
import numpy as np

a = 13.42
b = 42.13

def number_parts(input) -> np.ndarray:
    input = [input] if type(input) != list else input
    return np.uint8([str(x).split('.') for x in input])

def compare_numbers(a: float, b: float) -> np.bool:
    '''compares numbers for equality of integer and fractional part'''
    return np.any(
        number_parts(a) == number_parts(b)[:,::-1], 
        axis=1)

print(compare_numbers(a, b))

#print(compare_numbers([a,a,a], [b,b,b]))