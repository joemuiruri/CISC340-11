import sqlite3 as sql

def insertUser(password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO userpassword (password) VALUES (?)", (password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT password FROM userpassword ")
	users = cur.fetchall()
	con.close()
	return users