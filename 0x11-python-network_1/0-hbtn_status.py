#!/usr/bin/python3
"""python script that fetches a url"""


if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print('Body response:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
