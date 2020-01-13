#!/usr/bin/python3
"""
a Python script that takes in a string and sends a search request to the Star
Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
        try:
            star_req = requests.get("https://swapi.co/api/people/?search={}".
                                    format(argv[1])).json()
            print("Number of results: {}".format(star_req["count"]))
            for people in star_req["results"]:
                print(people["name"])
        except:
            print("Not a valid PARAMETER")
