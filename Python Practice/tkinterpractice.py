

import tkinter
from tkinter import * #* imports all widgets






class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)#when window pops open, user can not resize GUI
        self.master.geometry('{}x{}'.format(700,400)) #sets default dimensions of GUI frame
        self.master.title('Learning Tkinter!') #title of window
        self.master.config(bg='lightgray') #sets background color of window
           
        self.varFName = StringVar() #creates Tkinter variable
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='First Name: ',font=("Helvetica",16),fg='black',bg='lightgray')
        self.lblFName.grid(row=0,column=0, padx=(10,0),pady=(10,0)) #margins

        self.lblLName = Label(self.master,text='Last Name: ',font=("Helvetica",16),fg='black',bg='lightgray')
        self.lblLName.grid(row=1,column=0, padx=(10,0),pady=(10,0))

        self.lblDisplay = Label(self.master,text='',font=("Helvetica",16),fg='black',bg='lightgray')
        self.lblDisplay.grid(row=3,column=1, padx=(10,0),pady=(10,0))
        
        self.txtFName = Entry(self.master, text=self.varFName,font=("Helvetica",16),fg='black',bg='lightblue') #entry, basically input device
        self.txtFName.grid(row=0,column=1, padx=(10,0),pady=(10,0))

        self.txtLName = Entry(self.master, text=self.varLName,font=("Helvetica",16),fg='black',bg='lightblue')
        self.txtLName.grid(row=1,column=1, padx=(10,0),pady=(10,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) #self is basically the class, submit is the method, and this command is calling the method
        self.btnSubmit.grid(row=2,column=1, padx=(10,0),pady=(10,0), sticky=NE) #sticky tells where it wants to stay, kind of like float in HTML/CSS

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(0,90),pady=(10,0), sticky=NE)


    def submit(self):
        fn = self.varFName.get() #gets value and stores in new variable
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()
        
"""

        TEST CODE, PASTE IN def __init__ (self): under self.varLName = String() and replace Entry code

        self.varFName.set('Bob')     #assigning values
        self.varLName.set('Smith')


        print(self.varFName.get())  #get gets whatever value is already stored #self is there to know how to access data
        print(self.varLName.get())
        

        self.txtFName = Entry(self.master,text=self.varFName,font=("Helvetica",16),fg='black',bg='lightblue') #calling from tkinter, one of the widgets we imported.
                                                                                                                #place this entry on self.master, value can change since
                                                                                                                #we placed in a variable
        self.txtFName.pack() #pack places, not very specific about placement. paints it on window
        
        self.txtLName = Entry(self.master, text=self.varLName,font=("Helvetica",16),fg='black',bg='lightblue')
        self.txtLName.pack()
"""








if __name__ == "__main__":
    root = Tk() #connects Tk to root variable for next line to use 
    App = ParentWindow(root)
    root.mainloop #keeps tab open, if this is not here it will pop up and disappear 
