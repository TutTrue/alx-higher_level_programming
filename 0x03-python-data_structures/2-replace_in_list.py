#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ replace an element in the list """
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    my_list[idx] = element
    return my_list
