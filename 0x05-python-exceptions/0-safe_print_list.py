#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    while True:
        try:
            if index < x:
                print(my_list[index], end="")
                index++
        except:
            print()
        finally:
            return index

        
