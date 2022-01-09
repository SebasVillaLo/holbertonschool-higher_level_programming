#!/usr/bin/python3
""" that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.parse as par
    from sys import argv

    url = argv[1]
    value = {'email': argv[2]}
    data = par.urlencode(value).encode('utf-8')
    peticion = request.Request(url, data)
    with request.urlopen(peticion) as response:
        print(response.read().decode('utf-8'))
