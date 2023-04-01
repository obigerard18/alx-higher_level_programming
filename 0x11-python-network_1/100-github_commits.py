#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(sys.argv[2], sys.argv[1])
    res = requests.get(url)
    num_commits = 0
    for el in res.json():
        if num_commits < 10:
            print("{}: {}".format(el.get("sha"),
                  el.get("commit").get("author").get("name")))
        num_commits += 1
