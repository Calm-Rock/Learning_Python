

import urllib.request
import urllib.parse
import re

url = 'https://pythonprogramming.net'
values = {'s':'basics',
          'submit' :'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

'''print(respData)'''


paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

# . means any character except new line
# * 0 or more repitition
# * is for. ie it is combined with .  
# ? o or 1 repition ie finding anything between the paragarphs
#tag and doing only 0 or 1 repition of that.
# so, .*? means find everything between the given tags
#What we want to search
#for must be specified withinn the parenthesis.


for eachP in paragraphs:
    print(eachP)


















