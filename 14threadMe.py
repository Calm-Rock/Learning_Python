'''There are three possible things we can do to
a file, write, append and read so while using
open('exampleFile.txt','r') use r for read'''

'''readMe = open('readMe
              .txt','r').read()
print(readMe)'''

'''readMe1 = readMe.read()
print(readMe1)'''

'''Many times we want to read line by line
say if we want to read an excel sheet, this
can be done by using readlines.
This will do that instead of writng al the text
as one bit of information to a variable, it's
 actually going to save this into a python list
 stored under readMe'''

readMe = open('appendedFile.txt','r').readlines()
print(readMe)
