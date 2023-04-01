#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
from urllib import request, parse, error
import sys

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf8'))
    except error.HTTPError as e:
            print('Error code: {}'.format(e.code))
