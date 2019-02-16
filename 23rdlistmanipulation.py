
x = [3,4,5,6,7,2,4,7,9,77,8,9]

'''x.append(5) #Adds 2 to the list'''

'''x.insert(2,45) #Used to insert data exactly where
#you want to, x.insert(index,number to be inserted)'''


'''x.remove(2) #This removes the first 2 in the list'''

'''x.remove(x[2])#Removes 3rd element of the list'''


print(x[5:8])#This is called slicing of data

print(x[-1])#Use this to access  the last element of list
#x[-2] for 2ndlast list



print(x.index(5))#This will give the index value(s)
#of the nummber 5

print(x.count(4))#Tells us about the number of
#4 present in the list

x.sort()#We can't do print(x.sort()) because
#sort is a function being run on x
print(x)

y = ['Kat','ALice','Joey','Monica']
y.sort()
#Note that since we are using y.sort() where
#y is a list this implies that sort() or anything
#which we used with a dot with the list are
#functions present in the list module.

print(y)#Sorted alphabetically
