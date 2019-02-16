#Let's create a main menu

from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master 

        self.init_window()


    def init_window(self):

        self.master.title("GUI")

        self.pack(fill =BOTH, expand =1)

        #quitButton = Button(self, text = 'Quit', command=self.client_exit)
        #command tells us about what to do with the button.
        

        #quitButton.place(x=0, y=0)
        #till here, quit button is placed.

        menu = Menu(self.master)#This is he menu of main window
        self.master.config(menu=menu)
        
        file = Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
#adding commands like recent,exit,new,save etc. to our file

        menu.add_cascade(label='File',menu=file)
#Adding file to our menu

        edit =Menu(menu)#Part of our main menu
        edit.add_command(label='Undo')#We don't have any command
        menu.add_cascade(label='Edit', menu=edit)
#If we remove the edit.add_command line, we still will
#have a button by remaning two lines, but the buttons won't do anything.
        









        


    def client_exit(self):
         exit()

root = Tk()
root.geometry("400x300")


app = Window(root)

root.mainloop()

#The button would be created but it won't do anything.
