#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + 1 fix

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        prime_status = is_prime_check(result)
        if prime_status:
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


def is_prime_check(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number*0.5) + 1):
        if number % i == 0:
            return False
    return True

@is_prime
def sum_three(*numbers):
    """Возвращает сумму трех чисел."""
    return sum(numbers)


# Пример использования функций
result = sum_three(2, 3, 6)
print(result)  # Вывод будет зависеть от того, является ли 11 простым числом.
