#!/usr/bin/python3
"""python script that fetches a url passed py a user"""


if __name__ == '__main__':
    from urllib import request
    import sys

    url = sys.argv[1]
    with request.urlopen(url) as res:
        content = res.headers
        print(content['X-Request-Id'])
