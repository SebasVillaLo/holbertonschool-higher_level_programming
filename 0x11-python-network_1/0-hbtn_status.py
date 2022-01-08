#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        readcontent = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(readcontent)))
        print("\t- content: {}".format(readcontent))
        print("\t- utf8 content: {}".format(readcontent.decode('utf8')))
