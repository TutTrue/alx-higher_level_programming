#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 != 0:
        c -= 32
        print(f"{c:c}", end="")
    else:
        print(f"{c:c}", end="")
