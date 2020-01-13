#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status using the
requests lib """
import requests


if __name__ == "__main__":
    html = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
