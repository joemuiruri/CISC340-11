import sqlite3
import sys

conn=sqlite3.connect('database.db')
curs=conn.cursor()

# function to insert data on a table
def add_data (password):
	curs.execute("INSERT INTO users VALUES(date('now'),(?))", password)
    conn.commit()
# call the function to insert data
add_data (3000)
add_data (12345)
add_data (77789)

# print database content
print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM users"):
	print (row)
# close the database after use
conn.close()
