import sqlite3
import sys

con = sqlite3.connect('database.db')

with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE users(TIMESTAMP DATETIME, password NUMERIC)")
