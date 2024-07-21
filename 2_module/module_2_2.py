#!/usr/bin/env python3
import sys
import traceback

try:
    numbers = list(map(int, input(
        "Enter 3 or more numbers, separated by space and pres ENTER:"
        ).split(" ") if len(sys.argv) < 4 else sys.argv[1:])) 
    if len(numbers) < 3: raise RuntimeError("3 or more numbers required")
except:
    print("BAD INPUT!")
    traceback.print_exc()
    exit(1)

unique_numbers = len(set(numbers))

if unique_numbers > 2:
    print(f"There are {unique_numbers} unique numbers.")
elif unique_numbers == 2:
    print("There are only 2 unique numbers.")
else:
    print("There no unique numbers.")
