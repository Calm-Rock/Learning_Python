
#For appending, we will still  use .write()

appendMe = '\nYou only live once, so Carpe Diem!'

appendFile = open('appendedFile.txt','a')
#You can add a new line either by above method or
#by using appendFile.write('\n') here
appendFile.write(appendMe)
appendFile.close()
