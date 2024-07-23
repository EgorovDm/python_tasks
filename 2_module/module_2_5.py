#!/usr/bin/env python3

import numpy as np

# BAD solution
# get -> gen, because get is ambiguous,
# matrix is generated, not readed from memory
def gen_matrix(height: int = 2, width: int = 2, value: int = 0) -> list:
    '''Bad matrix generation function'''
    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(value)
        matrix.append(row)
    return matrix

def gen_matrix_better(height: int = 2, width: int = 2, value: int = 0) -> list:
    '''Better matrix generation function, but still bad'''
    return [[value] * width] * height

def gen_matrix_good(height: int = 2, width: int = 2, value: int = 0) -> list:
    '''Proper generation function'''
    return np.full((height, width), value)

test_data = ((2, 2, 10), (3, 5, 42), (4, 2, 13))
test_funcs = [gen_matrix, gen_matrix_better, gen_matrix_good]

for data in test_data:
    for func in test_funcs:
        print(
            "="*10 + "\n",
            func(*data),
            "\n" + "="*10, sep=""
        )
