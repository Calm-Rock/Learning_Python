#Both of them, a tuple and a list are a list
#Tuple can't be modified while a list can be modified


x = 2,6,3,4
'''x = (2,6,3,4)''' #These are tuples

y = [2,6,3,4] #This is a list, it can be identified
            # by the squar brackets
        
#Say if we have a list of data which won't be
#changing, then we can use tuples intead of a
#python list, because t will traverse faster.


'''def examplefunc():
    return 15,5           #Example of tuple use

x,y = examplefunc()'''


print(x[1])   #Indexing start at 0
print(y[2],y[3])


#Tupule can be used for unpacking of sequence.

