
def simple(num1,num2):
    pass
# pass just gives this function something to do so that
#it does not display an error message while we make other functtions

def simple(num1,num2=5):
    print(str(num1)+str(num2))
simple(5)#Here we only have to pass one variable since
#second one is having a default value.

def simpleQ(num1,num2=5):
    print(str(num1),str(num2))
simpleQ(5)


'''So, why do we need default variables?
Different people want different customization,  some want
their radio to be fixed in a particular  way and some want
their suspension to be fixed in a particular way.'''

#Let's take a look at this

def basic_window(width,height,font = 'TNR',
                 bgc = 'W', scrollbar=True):
    print(width,height,font, bgc)
   
basic_window(150,350)

# To change the bgc and not font, we can do something like

def basic_window1(width,height,font = 'TNR',
                 bgc = 'W', scrollbar=True):
    print(width,height,font,bgc)
   
basic_window1(150,350,bgc='B')

# Even if we give a 3rd argument to the function, we can do so

def basic_window2(width,height,font = 'TNR',
                 bgc = 'W', scrollbar=True):
    print(width,height,font, bgc)
   
basic_window2(150,350,'Callibre')
