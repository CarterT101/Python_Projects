

#SQL INJECTION HELP

import sqlite3

#personal data from user

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")" #change integer into string to make it a valid age for the database
    c.execute(line)
