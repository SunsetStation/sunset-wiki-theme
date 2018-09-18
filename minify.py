#!/bin/env python3

# Script for minifying the css for use in production

import requests

def main():
    url = 'https://cssminifier.com/raw'
    data = {'input': open('vector.css', 'rb').read()}

    response = requests.post(url, data=data)
    minified = open('vector-minified.css', 'w+')
    minified.write(response.text)
    minified.close()

if __name__== "__main__":
    main()
