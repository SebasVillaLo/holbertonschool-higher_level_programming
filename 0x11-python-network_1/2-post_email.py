#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


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
