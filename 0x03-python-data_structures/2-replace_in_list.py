#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if not my_list:
        return my_list
    elif not element:
        return my_list
    if idx >= 0 and idx < x:
        my_list[idx] = element
    else:
        return my_list
    return my_list
