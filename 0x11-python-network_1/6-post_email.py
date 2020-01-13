#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8) using the requests lib """
import requests
from sys import argv


if __name__ == "__main__":
    email = requests.post(argv[1], {"email": argv[2]}).text
    print(email)
