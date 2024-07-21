#!/usr/bin/env python3
import numpy as np

def get_primes(n: int) -> np.ndarray:
    '''numpy Sieve of Eratosthenes'''
    x = np.ones((n+1,), dtype=np.bool)
    x[0], x[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
    primes = np.where(x == True)[0]
    return primes

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes, not_primes = [], []

possible_primes = get_primes(np.max(numbers))

for number in numbers:
    primes.append(number) if number in possible_primes else not_primes.append(number)

print(f"PRIMES: {primes}\nNOT_PRIMES: {not_primes}")
