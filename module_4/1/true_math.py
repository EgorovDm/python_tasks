#!/usr/bin/env python3
import numpy as np

def divide(first: int, second: int) -> float:
    """Divide with corner cases"""
    try:
        return first/second
    except ZeroDivisionError:
        if not first:
            return 1
        else:
            return np.inf
