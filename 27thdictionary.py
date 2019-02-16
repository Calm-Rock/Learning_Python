#Dictionaries
#Unordered assortment od data with keys ad Values
#Keys are single values
#Values can be lists, multi dim list, functions
#We can reference another dictionary in a dictionary

exDict = {'Jack': 15, 'Bob':22, 'Alice':12, 'Kevin':16}
#Use {} for dictionary

print(exDict)

print(exDict['Jack'])
#This is referencing in a dictionary
#Here Jack is the key and it will give us the value 15

#Adding  Tim
#It will be added randomly
exDict['Tim'] = 14
print(exDict)

#That's how you change age of Tim
exDict['Tim'] = 15
print(exDict)

#Remove Tim

del exDict['Tim']
print(exDict)

#Nw we add hair color too
exDict1 = {'Jack': [15,'blonde'], 'Bob' : [22,'black'], 'Alice':[12,'brown'], 'Kevin': [16,'blue']}
print(exDict1['Jack'][1])
