#Regular expressions or Re
#They are their own programming language


#The basic idea f Re is to pass a string of arguments
#to a string of texts.
#Let's say we want to pull data from a body of text.
#Say we are only lookin for numbers or strings where
#first letter is capitalised.
#We would beusing Re for parsing paragrapg data away from
#website data.

'''
Identifiers:
#they say that we are looking for a number

\d --> any number
\D --> anything but a number
\s --> space
\S--> anything but a character
\w --> any character
\W --> anything but a character
.  --> any character, except for a new line
\b --> the white space around words
\. --> a period

Modifiers:
#its just a descripton

{1,3} --> we're expecting 1-3 of them (Example \d{1,3})
+ --> Match 1 or more
? --> Match 0 or 1
* --> Match 0 or more
$ --. Match the end of string
^ --> Matching the beginning of a string.
| --> either or
[] --> range or "variance" [A-Z] [A-Za-z] [1-5a-qA-Z]
{x} --> Expecting "x" amount

White Space Characters:

\n --> New line
\s --> space
\t -->tab
\e --> escape
\f --> form feed
\r --> return

DONT FORGET!
. + * ? [ ] $ ^ ( ) {} | \

'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 120.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names =  re.findall(r'[A-Z][a-z]*',exampleString)
#Here we are looking for anything A-Z or a-z
#* says that we are lookin for one of A-Z capital and
#as many of a-z 0 or more repitions
#As soon as we hit a white space, or a ", or a period"
#it will stop there.

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)    











































