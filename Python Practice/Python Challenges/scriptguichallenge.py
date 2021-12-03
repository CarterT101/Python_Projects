



from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450,175))
        self.master.title('Check files')
       

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=2,column=0, padx=10, pady=(40,5))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=3,column=0, padx=10, pady=(5,5))

        self.btnCheck = Button(self.master,text="Check for files...",width=12,height=2)
        self.btnCheck.grid(row=4,column=0,padx=10,pady=(5,10))

        self.txtEntry1 = Entry(self.master,width=30, font=("Arial",12))
        self.txtEntry1.grid(row=2,column=1,columnspan=4,padx=10,pady=(40,5))

        self.txtEntry2 = Entry(self.master,width=30, font=("Arial",12))
        self.txtEntry2.grid(row=3,column=1,columnspan=4,padx=10,pady=(5,5))

        self.btnClose = Button(self.master,text="Close Program", width=12, height=2)
        self.btnClose.grid(row=4, column=4, padx=10, pady=(5,5), sticky=SE)




if __name__ == "__main__":
    root = Tk() #connects Tk to root variable for next line to use 
    App = ParentWindow(root)
    root.mainloop #keeps tab open, if this is not here it will pop up and disappear 
