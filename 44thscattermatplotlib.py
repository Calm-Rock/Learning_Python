#Matplotlib

from matplotlib import pyplot as plt
from matplotlib import style 

style.use('ggplot')

x = [5,6,7,8]
y = [7,3,8,3]

print(len(x))
print(len(y))#Do these to tackel the error written in last comment

#plt.scatter(x,y,color='k')
plt.bar(x,y,color='g')

plt.title('Dumb Chart')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')



plt.show()
#plt.show() brings up the graph
#We need to reshow for updating, when using live feeds

#If we have more x's than y's, then we will get a
#value error saying x and y must have same first dimension


