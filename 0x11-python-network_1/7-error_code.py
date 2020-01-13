#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
displays the body of the response usung the requests lib """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        err = requests.get(argv[1])
        err.raise_for_status()
        print(err.text)
    except:
        print("Error code: {}".format(err.status_code))
