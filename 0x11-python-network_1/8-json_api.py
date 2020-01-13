#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests
from sys import argv


if __name__ == "__main__":
    input_1 = ""
    if len(argv) == 2:
        input_1 = argv[1]
    try:
        err = requests.post("http://0.0.0.0:5000/search_user",
                            data={'q': input_1}).json()
        if ("id" in err) and ("name" in err):
            print("[{}] {}".format(err['id'], err['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
