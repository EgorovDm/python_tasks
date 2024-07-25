#!/usr/bin/env python3

def divide(first: int, second: int) -> float:
    """Divide with exeption handling"""
    try:
        return first/second
    except ZeroDivisionError:
        return "Ошибка деления на 0!"
