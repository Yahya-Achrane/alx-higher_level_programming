#!/usr/bin/python3

def search_replace(my_list, search, replace):
    num = 0
    listt = []
    for i in my_list:
        if i == search:
            listt += [replace]
        else:
            listt += [my_list[num]]
        num += 1
    return listt
