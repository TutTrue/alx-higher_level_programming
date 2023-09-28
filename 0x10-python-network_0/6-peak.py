#!/usr/bin/env python3
def find_peak(list_of_integers):
    """find a peak"""
    for i in range(len(list_of_integers)):
        try:
            if list_of_integers[i - 1] <= list_of_integers[i] and list_of_integers[i] >= list_of_integers[i+1]:
                return list_of_integers[i]
        except:
            try:
                if list_of_integers[i] >= list_of_integers[i+1]:
                    return list_of_integers[i]
            except:
                if list_of_integers[i] > list_of_integers[i - 1]:
                    return list_of_integers[i]
    return None
