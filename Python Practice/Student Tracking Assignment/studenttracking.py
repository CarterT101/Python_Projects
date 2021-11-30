
#
#   Python 3.9.9
#
#   Author: Carter Thurman
#
#   Purpose: Tech Academy Assignment, Tkinter and SQL practice
#
#
#   Tested and works with Windows 10 and 11
#


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import studenttrackingfunc
import studenttrackinggui



#main
    
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(500,300) #height, width
        self.master.maxsize(500,300)
        studenttrackingfunc.center_window(self,500,300) #this center method will center our app on user's screen
        self.master.title("The Tkinter Student Tracking Demo")
        self.master.configure(bg="#F0F0F0")
        #protocol method is a tkinter built-in method to catch if user clicks upper corner 'X' on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttrackingfunc.ask_quit(self))
        arg = self.master

        #load GUI widgets 
        studenttrackinggui.load_gui(self)

        #Instantiate the Tkinter dropdown object, menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",underline=1,accelerator="Ctrl+Q",command=lambda: studenttrackingfunc.ask.quit(self))
        menubar.add_cascade(label="File",underline=0,menu=filemenu)
        helpmenu = Menu(menubar,tearoff=0) #defines drop down column and tearoff=0 means do not add separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About this Student Tracking Demo") #add_command is a child menubar item of the add_cascade parent item
        menubar.add_cascade(label="Help", menu=helpmenu) #add_cascade is a parent menubar item (visible heading)

        #apply config method of the widget to display the menu. could also pass additional aprams for additional functionality or appearances such as borderwidth
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
