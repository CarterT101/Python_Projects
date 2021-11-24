

import sqlite3


#print(dir(sqlite3))

#print(help(sqlite3))


conn = sqlite3.connect('files.db') #connecting variable to database


with conn:
    cur = conn.cursor() #can edit table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )") #executes sql statements
    conn.commit() #commits it to database
conn.close() #closes database


fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg') #list of files


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    for file in fileList: #goes through created list 
        if file.endswith('.txt'): #finds files that end with .txt
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (file,)) #inserts each into table through iterations
            print(file)
    conn.commit()
conn.close()




                
