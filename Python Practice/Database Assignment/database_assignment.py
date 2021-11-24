

import sqlite3


#print(dir(sqlite3))

#print(help(sqlite3))


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()



fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

txtList = []

for file in fileList:
    if file.endswith('.txt'):
        txtList.append(file)

print(txtList)

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_file) VALUES (?) ", \
                ('{}'.format(txtList[0])))
    cur.execute("INSERT INTO tbl_files(col_file) VALUES (?) ", \
                ('{}'.format(txtList[1])))
    conn.commit()
conn.close()

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        items = "First Document: {}\nSecond Document: {}".format(item[0],item[1])
    print(items)


                
