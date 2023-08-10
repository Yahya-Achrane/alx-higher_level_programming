#!/usr/bin/python3

def remove_char_at(str, n):
    stored = ""
    for i in range(len(str)):
        if n != i:
            stored += str[i]
    return stored
