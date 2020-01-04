import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
   
url = 'http://py4e-data.dr-chuck.net/comments_346954.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
   
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments')
comment = results[0].findall('comment')
total = 0
for node in comment:
    count = node.find('count').text
    total = total + int(count)
print(total)
