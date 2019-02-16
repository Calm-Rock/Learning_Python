#Classes are almost equivivalent to a module

class calculator:  #No parameters needed here

    def addition(x,y):
        added = x + y
        print(added)

    def subtraction(x,y):
        subtracted = x-y
        print(subtracted)

    def multiplication(x,y):
        multiplied = x*y
        print(multiplied)

    def division(x,y):
        divided = x/y
        print(divided)

#This how we use our class    
calculator.multiplication(3,5)
