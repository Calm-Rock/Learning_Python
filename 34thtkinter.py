#Tkinter
#tkinter is a wrapper around tk which is a wrapper around
#tcl for making windows.

#Within 10 line of code, we can make a window which can be
#minimized, maximised and closed.


from tkinter import *

class Window(Frame):
#Frame is an inbuit funtion in tkinter in init script
#Whenever you pass your object through a class,
#you say it 'self'
    
    def __init__(self, master = None):
#now we decide which parameters to pass through the frames class
#this is our main window, then we will putore stuff in the window
        Frame.__init__(self, master)

        self.master = master #This is our main windowor master widget or main frame
    

root = Tk()   #This calls our root window     


app = Window(root)

root.mainloop()
#This initialises and generates our window for us.























