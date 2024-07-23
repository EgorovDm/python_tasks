#!/usr/bin/env python3
import traceback

mutable_var = [
    1, 
    'a', 
    {1,2}, 
    (), 
    object()
]
# print(id(mutable_var))
mutable_var[:] = [None]*len(mutable_var) 
# print(id(mutable_var))
print(
    "Mutable var:",
    mutable_var,
    sep="\n"
)

immutable_var = (
    1,
    "one",
    [1,2,3,4],
    print,
    None,
    {1,2,3,3}
)
legal_code = "immutable_var[2].pop(2)"
illegal_code = "immutable_var[2] = 30"
print(immutable_var)

print(f"We can change mutable objects inside immutable \n{legal_code}\nResult:")
eval(legal_code)
print(immutable_var)
print("But we can change imutable object itself:")

try:
    exec(illegal_code)
except: 
    traceback.print_exc()

_ = input("Why? Just read the docks, it's easy 📚✊ (PRESS ENTER)")
help(tuple)
