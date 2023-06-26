#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li = []
    index = 0
    if list_length < index:
        print("out of range")
    while index < list_length:
        try:
            li.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            li.append(0)
        except TypeError:
            print("wrong type")
            li.append(0)
        except IndexError:
            print("out of range")
            li.append(0)
        finally:
            index += 1
    return li
