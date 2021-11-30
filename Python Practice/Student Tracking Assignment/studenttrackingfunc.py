

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

import studenttrackinggui
import studenttracking




#app window formatting

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth() #gets users screen width and height
    screen_height = self.master.winfo_screenheight()
    
    x = int((screen_width/2) - (w/2)) #calculates x and y coords to paint app centered on user's screen
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self): #ensures if the user wants to quit app
    if messagebox.askokcancel("Exit program","Okay to exit application?"):
        self.master.destroy() #closes app
        os._exit(0)

#database and functions

def create_db(self):
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit() #committing and closing database connection 
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Carter','Thurman','Carter Thurman','111-111-1111','cartthur@email.com','Software Developer'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody: #returns tuple we can slice into parts using data[] during iteration
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])
            
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip() #remove any blank space before and after user's entry
    var_lname = var_lname.strip() #ensures that first character in each word is capitalized 
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) #combines names into fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0): #enforces user to provide both names
        conn = sqlite3.connect('db_studenttracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname) #update listbox with new fullname
                onClear(self) #call the function to clear all of text boxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) #call function to clear all of text boxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing text error","Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #listboxes selected value
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cur = conn.cursor()
        #check count to ensure that this is not the last record in the database, cannot delete last record or we get error
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \nProceed with the delete request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_studenttracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #call function to clear all of textboxes and the selected index of listbox
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    #clear text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    #poplate listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_fullname FROM tbl_students""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + i
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of list selection
        var_value = self.lstList1.get(var_select) #list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the update request.")
        return
    #user will only be allowed to update changes for phone, email, and courses, for name changes the user will need to delete the entire record and start over
    var_phone = self.txt_phone.get().strip() #normalize data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0): #ensure data is present
        conn = sqlite3.connect('db_studenttracking.db')
        with conn:
            cur = conn.cursor()
            #count records to see if the user's changes are already in the db, meaning there are no changes to update
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_students WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_students WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(col_course) FROM tbl_students WHERE col_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)
            if count == 0 or count2 == 0 or count3 == 0: #if proposed changes are not already in database, proceed
                response = messagebox.askokcancel("Update request","The following changes ({}),({}), and ({}) wil be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_course,var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET col_phone = '{0}',col_email = '{1}',col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","({}), ({}), and ({}) \nall already exist in the database for this name. \n\nYour update request has been canceled.".format(var_phone,var_email,var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, email, or course information.")
    onClear(self)


if __name__ == "__main__":
    pass

    
