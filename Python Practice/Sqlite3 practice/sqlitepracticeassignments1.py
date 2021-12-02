


import sqlite3

peopleValues = (('Luigi', 'Vercotti', 42), ('Arthur','Belling',28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE PEOPLE(FirstName TEXT, LastName TEXT, AGE INT);
                    INSERT INTO People VALUES('Ron','Obvious','42');
                    """)
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
