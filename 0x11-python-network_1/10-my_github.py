#!/usr/bin/python3
"""that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv