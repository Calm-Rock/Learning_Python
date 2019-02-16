#Urllib
#It lets you do all amazing things that can be done
#with internet with python as the programming language

'''import urllib.request
#This will give the source code of google.com
x = urllib.request.urlopen('https://www.google.com')
#It make request to this url and by default it will
#be a get request

print(x.read())'''

#Say we go to the website pythonprogamming.net
#on this website, we search basic
#after doing so, we see that the url of the website
#has changed to, prthonprogamming.net/?s=basic&submit=Search
#Here s and submit are the variables
#If we look at these variables, we will see that
#the firstvariable in the link will have a '?'
#and the subsquent variables will have '&' sign
#This is an example of GET request, we get data based on
#these variable


import urllib.request
import urllib.parse

'''url = 'https://google.com/search'#base url we want to visit
values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)'''
'''
url = 'https://pythonprogramming.net'
values = {'s':'basic',
          'submit':'search'}
#This is a dictionary named values

data = urllib.parse.urlencode(values)

#this is data from the site
#urlencode encods the values as it should be in the url
#This can be better understood as
#go to google.com and serach 'Hey check that out',
#you will see in the url that the query ie q is q = hey+check+that+out
#You can do the query b removng the + query in the url
#and just typing 'Hey check that out' with spaces
#in the url and hit enter, you will see that the spaces
#are changed to %20 because that is the encoding for
#space.
#similarly we will have encoding for '?' also etc
#As soon as we introduce '&' signs and '?', it
#would be good to do it the official way like we
#are doing now rather than hard-coding.

data = data.encode('utf-8')
#this is a type of encoding which puts your data in bytes
req = urllib.request.Request(url,data)
#What we wanna request is first the url and then the data
#first the url an then the data wewanna pass through
#and we have encoded the data under utf-8

resp = urllib.request.urlopen(req)
#now we are visiting the url

respData = resp.read()

print(respData)'''

#With HTML, it tells the browser how it should display
#data, and your browser handles the html and makes it
#pretty for you and by seperating tags from text and
#organizes things.
#but with python, it just looks at the source
#we have no rganization here.

#When we access the website with some programming language
#sometimes the website owners don't like that 'cause they
#want real users not some bots or programmers
#so they will block you if they see that you arre not a user

#So, how to fool them?


try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #We are searching test in the google search bar
    
    print(x.read())
except Exception as e:
    print(str(e))
#We will get FObidden Error 403 since we are using
#programming and google forbids it.
#How to get around it?
    
try:
    url = 'https://www.google.com/search?q=test'

    headers = {}  #empty dictionary
#Headers contain the informatioiin about you,
#Who you are, your ip, your browser, your OS etc. and you send a header
#everytime you visit a website.
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    #This datais huge and it willl hang the console,
    #so we save this to a file.

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))
    #Here we are hard-coding it so we dn't include data
    #Include data when you are making a POST request
'''Why not just go to urllib.request function and make
changes to the Request 'function' which has function
parameters which has default value for the header parameter
why not set this value to the above header value.'''
'''Try this out'''
#Within headers, we have a piece of data called
#as User-Agent, it is the type of browser that we are using
#In our case,what python does is that it says
#python-urllib/pyhton version, so within an instan the
#website knows taht you are a program.
    
    
'''Now finally what we get is a txt file which is a huge mess
so now we will have to parse through the data'''


















