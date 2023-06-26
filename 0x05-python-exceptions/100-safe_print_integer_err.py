#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {:s}".format(str(ex)), file=sys.stderr)
        return False
