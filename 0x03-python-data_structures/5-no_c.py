#!/usr/bin/python3
def no_c(my_string):
    """  removes all characters c and C from a string. """
    new_str = ""
    for i in my_string:
        if ord(i) != 99 and ord(i) != 67:
            new_str += i
    return new_str
