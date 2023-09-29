#!/usr/bin/python3
"""fetch an url using requests package and display the variable from header"""


if __name__ == '__main__':
    import requests
    import sys

    data = {
        'name': sys.argv[2]
    }
    res = requests.post(sys.argv[1], data=data)
    print(res.text)
