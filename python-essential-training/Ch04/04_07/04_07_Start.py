# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json
import textwrap

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext, width=50))

print()
# Loading the decodedtetxt to a python iterable native object (Dictionary)
content = json.loads(decodedtext)
print(content['kind'])
print(content['items'][0]['searchInfo']['textSnippet'])
print(content['items'][0]['accessInfo']['webReaderLink'])
