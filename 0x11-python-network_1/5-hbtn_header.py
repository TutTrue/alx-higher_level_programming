#!/usr/bin/python3
"""fetch an url using requests package and display the variable from header"""


if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
