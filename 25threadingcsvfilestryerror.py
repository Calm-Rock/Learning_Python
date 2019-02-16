
#reading from a csv(comma seperated variable) spreadsheet
#Here the comma is the delimiter, we can have anything
#as a delimiter like space, variable x dots etc


import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    '''for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1])'''
        
#Here row actually means columns

#Data will bear in as string so for doing math
#operations on this data, convert it to int or float
    

#Say we want to put the dates and color in
#seperate columns.


    dates = []
    colors = []
    
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
#Use this when a user enters a different color
#Try and except is like the last effort to save the program,
#we must try something before it for error handeling
    
    try:
        whatcolor = input('What color do you wish to know the date of? ')
#Right after this,we must think that if this could
#create a problem?
        if whatcolor in colors:
           coldex =colors.index(whatcolor.lower())
##The .lower makes the upprcase letters to be read as lowercase
           theDate = dates[coldex]
           print('The  date of',whatcolor,'is', theDate)
        else: 
           print('Color not found, or is not a color.')

    except Exception as e: #Use NameError instead of Exceptio to find nameerror
        print(e)

    print('continuing')

    

            
                                
