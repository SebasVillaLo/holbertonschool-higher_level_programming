#!/usr/bin/python3
import urllib.request


with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    readcontent = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(readcontent)))
    print("\t- content: {}".format(readcontent))
    print("\t- utf8 content: {}".format(readcontent.decode('utf8')))
