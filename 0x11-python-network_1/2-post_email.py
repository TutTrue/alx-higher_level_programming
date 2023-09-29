#!/usr/bin/python3
"""python script that fetches a url passed py a user"""


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    data = {
        'email': sys.argv[2]
    }
    data = parse.urlencode(data).encode('utf-8')
    with request.urlopen(url, data=data) as res:
        print(res.read().decode('utf-8'))
