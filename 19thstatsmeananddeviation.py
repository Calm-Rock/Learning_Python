import statistics
#Inbuilt  module of python3

example_list = [13,34,56,7,8,9,2,1,2,3,45,6,56]

x = statistics.mean(example_list)

print(x)

y = statistics.median(example_list)
z = statistics.stdev(example_list)
w = statistics.variance(example_list)
print(y)
print(z)
print(w)
