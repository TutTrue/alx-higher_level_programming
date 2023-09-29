#!/usr/bin/python3
"""python script that fetches a url"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        print(res.read())
