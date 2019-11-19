# Team 11
# CISC 340 - Term Project
# This python script creates a database and need to start the app...
#  1. check python update (We are using python 2.7)
#  2. Start virtual environment... source venv/scripts/activate || python venv/scripts/activate_this.py
#  3. Create database... python createdb.py || python3 createdb.py
#  4. Start WebApp... python runapp.py || python3 runapp.py
import sqlite3
import time
import sys 

# Start database connection
conn = sqlite3.connect('pidatabase.db')
print("Opened database successfully")
c = conn.cursor()
#get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='userpassword' ''')

#Check if database is already created... If so, the old instance will be dropped and a new one will be created
if c.fetchone()[0]==1 : 
    conn.execute('drop table if exists userpassword')
    conn.execute('CREATE TABLE userpassword (id INTEGER PRIMARY KEY AUTOINCREMENT, password int)')
    c.execute("INSERT INTO userpassword (id,password) VALUES (?,?)",('1','12345') )
    conn.commit()
else:
    conn.execute('CREATE TABLE userpassword (id INTEGER PRIMARY KEY AUTOINCREMENT, password int)')
    c.execute("INSERT INTO userpassword (id,password) VALUES (?,?)",('1','12345') )
    conn.commit()
    
conn.close()