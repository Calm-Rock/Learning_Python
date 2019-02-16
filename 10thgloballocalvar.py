#Global variable can be accessed anywhere
#Local variable can be accessed within the environment only



x = 6
'''This variable has no parent function,but it is not a
 global variable, it just happens that it is committed to memory
 before any function is defined.'''

def example():
    z = 5
    print(z)
example()

'''def example2():
    global x
    print(x)
    x+=5
    print(x)
example2()'''

#Suppose we don't want to use Global Variable
#We can do something like

def example4():
    globx = x
    print(globx)
    globx+=5
    print(globx)
#Here globx is a local variable ie we won't be able to access globx
#outside this function,so what if we want to multiple functions to work
    #together, we'll have to do something like
    return globx
    
    
x=example4()
print(x)


def example1():
     print(x)
     print(x+5) 
#Umtil this it works perfectly fine
     x+=6
#This will create an error because x is not a global variable
     
example1()


