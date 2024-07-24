#!/usr/bin/env python3

my_list, index =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5], 0

while index < len(my_list):
    if my_list[index] < 0:
        break
    elif my_list[index]:
        print(my_list[index])
    else:
        pass
    index +=1
