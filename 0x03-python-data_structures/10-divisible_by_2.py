#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    mul of 2
    """
    x = []
    for i in my_list:
        if i % 2 == 0:
            x.append(True)
        else:
            x.append(False)
    return x
