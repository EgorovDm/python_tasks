#!/usr/bin/env python3
import traceback

def test_function() -> None:
    """Dummy test function"""
    def inner_function() -> None:
        """Dummyer test function inside dummy test function"""
        print("Я в области видимости функции test_function 🤤")
    inner_function()

test_function()
try:
    inner_function()
except NameError:
    traceback.print_exc()
    _ = input("Why? Just read the docks, it's easy 📚✊ (PRESS ENTER)")
    help(NameError)
    pass