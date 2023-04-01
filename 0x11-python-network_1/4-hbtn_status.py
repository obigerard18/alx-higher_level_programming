#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(req.text), req.text))
