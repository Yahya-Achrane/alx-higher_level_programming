#!/usr/bin/python3

def no_c(my_string):
    x_list = []
    x = 0
    while x < len(my_string):
        if my_string[x] != "C" and my_string[x] != "c":
            x_list += [my_string[x]]
        x += 1
    my_string = "".join(x_list)
    return my_string
