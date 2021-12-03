
import os                           #IMPORTING ALL NECESSARY MODULES
import webbrowser as wb
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self,master, *args, **kargs):
        Frame.__init__(self)

        fileName = StringVar() #created two temporary variables that grab Entry text, this one is for the file name
        fileText = StringVar() #this is for the file text
        
        def createHTML(self):
            if os.path.exists("{}.html".format(fileName.get())): #clears text file if named the same as what they inputted in Entry
                os.remove("{}.html".format(fileName.get()))
            else:
                pass
            f = open("{}.html".format(fileName.get()),"a") #creates new html file
            f.write("<html>\n<body>\n<h1>\nStay tuned for our amazing summer sale!\n</h1><p>{}</p>\n</body>\n</html>".format(fileText.get())) #inputs text from second Entry
            f.close()
            f = open("{}.html".format(fileName.get()),"r") #these two lines open file in web browser
            wb.open("{}.html".format(fileName.get()))
            
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550,175)) #making app box
        self.master.title('Write your own website')

        self.lblInsert = tk.Label(self.master,text='Input File Name Here:')
        self.lblInsert.grid(row=1,column=0,padx=10,pady=(20,10))
        self.lblInsert1 = tk.Label(self.master,text='Input Text Name Here:')
        self.lblInsert1.grid(row=2,column=0,padx=10,pady=(20,10))
                     
        self.txtEntry = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=fileName)
        self.txtEntry.grid(row=1,column=1,columnspan=4,padx=10,pady=(20,10))

        self.txtEntry1 = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=fileText)
        self.txtEntry1.grid(row=2,column=1,columnspan=4,padx=10,pady=(20,10))
        
        self.btnAddText = tk.Button(self.master,width=12,height=1,text='Add File', command=lambda:createHTML(self))
        self.btnAddText.grid(row=2,column=5,padx=10,pady=(20,10))


if __name__ == "__main__":
    root = Tk() #connects Tk to root variable for next line to use 
    App = ParentWindow(root)
    root.mainloop #keeps tab open, if this is not here it will pop up and disappear 



