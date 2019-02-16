def simple_addition(num1,num2):
    answer = num1 +num2
    print('num1 is',num1)
    print('sum is',answer)

simple_addition(5,3)


#We can have any amount of variables.

simple_addition(3,5) #We changed the orderof the numbers
#So, nnow num1 will be 3

# but if we stiill want num1 to be 5, we can do so by

simple_addition(num2=3,num1=5)

# in this, the quantity of variables also matter

simple_addition(3,4,5)
#This will display an error message.
#We will use default variables to counter this issue

