#System Module

import sys
#Keep stderr strictly for errors
#and stdout for everything else
#Basically they are the same

'''sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
#This will give red error test.
sys.stdout.write('This is stdout text\n')

print(sys.argv)'''
#This gives s the path of current file

#We can pass arguments into this file from outside

'''if len(sys.argv) > 1:
    print(sys.argv[1]) #This print out the second argument of the list
    print(float(sys.argv[1]) + 5)'''

def main(arg):
    print(arg)

main(sys.argv[1])#Here we used sys.argv[] to pass
#through the function

# We can use the coomand line to communicate
#with this and this thing can aslo be used
#t ssay communicate between python and say php
#while making the backend of a website

