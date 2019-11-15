import sqlite3

conn = sqlite3.connect('pidatabase.db')
print("Opened database successfully")

conn.execute('CREATE TABLE userpassword (todayDate DATE,password NUMERIC)')
print("Table created successfully")
conn.close()