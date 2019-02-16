'''import statistics as s

#This can be used as shortform
#for statistics, so instead of using statistics
#we will us s Example -> s.varance()

example_list = [2,5,6,8,9,4,2,6,8,9]
x = s.variance(example_list)
print(x)'''

#Say if we want to just use variance instead of
#s.variance() or statistics.variance()

from statistics import variance

example_list = [2,5,6,8,9,4,2,6,8,9]
x = variance(example_list)
print(x)


#next step would be to make variance as v

from statistics import variance as v

example_list = [2,5,6,8,9,4,2,6,8,9]
x = v(example_list)
print(x)

#now,if we want to import more than one function
#from the module, then

from statistics import variance as v, mean as m

example_list = [2,5,6,8,9,4,2,6,8,9]
x = v(example_list)
y = m(example_list)
print(x)
print(y)

#If we want to import everything from variance
#but we din't want to use the word statistics,then

from statistics import *
example_list = [2,5,6,8,9,4,2,6,8,9]
x = variance(example_list)
y = mean(example_list)
z = stdev(example_list)
w = median(example_list)
print(x)
print(y)
print(z)
print(w)

