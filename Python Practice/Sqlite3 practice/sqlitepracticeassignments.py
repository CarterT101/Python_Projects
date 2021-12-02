


import sqlite3
connection = sqlite3.connect("test_database.db") #creates database

c = connection.cursor() #instantiates a cursor object, control structure that enables operations on database. 'c' will let us execute commands on SQL database

c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)") #creates table and inserts three new columns into table, text, text, and integer

c.execute("INSERT INTO People VALUES('Ron','Obvious', 42)")

connection.commit() #commit changes so they would be saved

#connection = sqlite3.connect(':memory:') #creates temporary database, stored in RAM

c.execute("DROP TABLE IF EXISTS People") #deletes table Persons if it exists

connection.close()

"""
with sqlite3.connect("test_database.db") as connection: #good idea to use 'with' keyword to simplify code and life. helps find potential errors and frees up resources.

connection.close()
"""





