

import os               #all necessary modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import datetime
import time
import glob
import shutil

import filetransferassignmentgui
import filetransferassignmentfunc



class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450,175)) #making app box
        self.master.title('Move files')
        

        filetransferassignmentgui.load_gui(self)

  
if __name__ == "__main__":
    root = tk.Tk() #connects Tk to root variable for next line to use 
    App = ParentWindow(root)
    root.mainloop() #keeps tab open, if this is not here it will pop up and disappear 
