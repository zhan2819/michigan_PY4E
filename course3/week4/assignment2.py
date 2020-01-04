# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = input('Count - ')
position = input('pos - ')
c = int(count)
p = int(position)-1

for i in range(c):
    if i == 0:
        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        url = tags[p].get('href', None)
        print(url)
    else:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        url = tags[p].get('href', None)
        print(url)

