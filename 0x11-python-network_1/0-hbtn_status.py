#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status """


from urllib import request


with request.urlopen('https://intranet.hbtn.io/status') as req:
    html = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
