import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_346955.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
info = json.loads(data)
comments_dic = info['comments']
print(comments_dic)
total = 0
for item in comments_dic:
  total += item['count']
print(total)
