#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    ar = "{} {}{}".format(
            arg_len, "argument" if arg_len == 1 else "arguments",
            "." if arg_len == 0 else ":")
    print(ar)
    for i in range(1, arg_len + 1):
        print("{}: {}".format(i, sys.argv[i]))
