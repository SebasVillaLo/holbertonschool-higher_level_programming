#!/usr/bin/python3
"""that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    r = requests.get(url, auth=(argv[1], argv[2]))
    res = r.json()
    print(res.get('id'))
