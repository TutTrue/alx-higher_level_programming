#!/usr/bin/python3
"""python script that fetches a url"""


if __name__ == '__main__':
    from urllib import request, error

    try:
        with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
            content = res.read()
            print(content.decode('utf-8'))
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
