# Team 11
# CISC 340 - Term Project
# This python script runs our web application and to start the app please..
#  1. check python update (We are using python 2.7)
#  2. Start virtual environment... source venv/scripts/activate || python venv/scripts/activate_this.py
#  3. Create database... python createdb.py || python3 createdb.py
#  4. Start WebApp... python runapp.py || python3 runapp.py
import datetime
import sys
import os
import time
import serial
import gpout
from flask import Flask, render_template, request
from jinja2 import Environment, PackageLoader 
import sqlite3 as sql
#import RPi.GPIO as GPIO

app = Flask(__name__)
#env = Environment(loader=PackageLoader('StandaloneSite', 'templates'))

# SET GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#button = 20
#senPIR = 16

#buttonSts = GPIO.LOW
#senPIRSts = GPIO.LOW
   
# Set button and PIR sensor pins as an input
#GPIO.setup(button, GPIO.IN)   
#GPIO.setup(senPIR, GPIO.IN)

# Start of web app
@app.route('/')
def home():
   print("print test")
   return render_template('home.html')
# Update Database by adding new password
@app.route('/enternew')
def new_student():
   return render_template('password.html')
# Method to connect to our db (pidatabase) and add a password with the current date 
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         #todayDate = request.form['todayDate']
         password = request.form['password']
         # Start DB connection
         with sql.connect("pidatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO userpassword (password) VALUES (?)",(password) )     
            con.commit()
         #   msg = "Record successfully added"
         #   con.close()
      except:
         msg = "ERROR"
         return render_template("password.html",msg)
      finally:
         #con.close()
         return render_template("result.html")
   else:
      con.close()
      return render_template(".html")
# Profile of User 
@app.route('/list')
def list():
   con = sql.connect("pidatabase.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("SELECT * FROM userpassword")  
   rows = cur.fetchall()
   con.close()
   return render_template("list.html",rows = rows)
""" @app.route('/result')
def result():
   ser = serial.Serial(
      port = '/dev/ttyUSB1',
      baudrate = 9600,
      parity = serial.PARITY_NONE,
      stopbits = serial.STOPBITS_ONE,
      bytesize = serial.EIGHTBITS,
      timeout=1
   )

   while 1:
      ins = ser.readline()
      processedins = str(ins)[2]
      if(processedins == '1'):
         return render_template("alarmtrigger.html") """
# Method to check User Password vs Database password... 
# If passwords don't match, trigger the alarm  
@app.route('/login',methods = ['POST','GET'])
def login():
    i=1
    if request.method == 'POST':
      #  todayDate = request.form['todayDate']
      password = request.form['password']
      print("password collected")
      with sql.connect("pidatabase.db") as con: 
         print("DB created")
         cur = con.cursor()
         print("Cursor Created")
         cur.execute("SELECT password from userpassword where password = " + password)
         print("Password: " + password)
         print("SQL request taken")
         print("Create temp list to check password")
         #print(cur.fetchall())
         fetched = cur.fetchall()
         passwd = int(password)
         #db_check = cur.fetchone()
         print(fetched)
         print(type(fetched))
         print(type(password))
         print(type(passwd))
         '''while(i>=1):
           # print("fetch all works")
            for z in fetched:
               print("db check")
               if passwd == int(z[0]):
                  print("success")
                  i=0
                  cur.close()
                  return render_template("result.html")
               else:
                  print("failure")
                  i=0
                  cur.rollback()
                  cur.close()
                  return render_template("wrongpassword.html")
         '''
         if len(fetched) > 0:
            print("success")
            cur.close()
            return render_template("result.html")
         else:
            print("failure")
            #cur.rollback()
            cur.close()
            return render_template("wrongpassword.html")
      
         # cur.close()
         return render_template("login.html")

      try:
       #  todayDate = request.form['todayDate']
         password = request.form['password']
         print("password collected")
         with sql.connect("pidatabase.db") as con: 
            print("DB created")
            cur = con.cursor()
            print("Cursor Created")
            cur.execute("SELECT password from userpassword where password = " + password)
            print("Password: " + password)
            print("SQL request taken")
            print("Create temp list to check password")
            print(cur.fetchall())
            fetched = cur.fetchall()
            passwd = int(password)
            #db_check = cur.fetchone()
            print(fetched)
            print(type(fetched))
            print(type(password))
            print(type(passwd))
            '''while(i>=1):
              # print("fetch all works")
               for z in fetched:
                  print("db check")
                  if passwd == int(z[0]):
                     print("success")
                     i=0
                     cur.close()
                     return render_template("result.html")
                  else:
                     print("failure")
                     i=0
                     cur.rollback()
                     cur.close()
                     return render_template("wrongpassword.html")
         '''
            if passwd in fetched[0]:
               print("true")
           # cur.close()
            return render_template("login.html")

      except:
        # con.close()
        # print(post_id)
         print("error")
         return render_template("wrongpassword.html")
     # finally:
     #    con.close()
       #  return render_template("login.html")
    else:   
      return render_template("login.html")
# view sensor data - Used mostly for testing     
@app.route('/gpiopage')
def gpiopage():
    # Read Sensors Status
#	buttonSts = GPIO.input(button)
#	senPIRSts = GPIO.input(senPIR)
	templateData = {
      'title' : 'GPIO input Status!',
      'button'  : '1',
      'senPIR'  : '2'
      }
	return render_template('gpiopage.html', **templateData)
# Extra Features 
# Delete record from database
@app.route("/deleterecord",methods = ['POST','GET'])  
def deleterecord():  
   if request.method == 'POST':
      try:  
         password = request.form['password']
         with sql.connect("pidatabase.db") as con:  
            cur = con.cursor()  
            cur.execute("delete from userpassword where password = ?",toInt(password))  
            con.commit()  
            msg = "record successfully deleted"
            return render_template("delete_record.html")  
      except:
         con.close()
         return render_template("wrongpassword.html") 
   else:
      return render_template("delete.html")  

# If passwords don't match, trigger the alarm  
@app.route('/alarmtrigger',methods = ['POST','GET'])
def alarmtrigger():
    i=1
    if request.method == 'POST':
      #  todayDate = request.form['todayDate']
      password = request.form['password']
      print("password collected")
      with sql.connect("pidatabase.db") as con: 
         print("DB created")
         cur = con.cursor()
         print("Cursor Created")
         cur.execute("SELECT password from userpassword where password = " + password)
         print("Password: " + password)
         print("SQL request taken")
         print("Create temp list to check password")
         #print(cur.fetchall())
         fetched = cur.fetchall()
         passwd = int(password)
         #db_check = cur.fetchone()
         print(fetched)
         print(type(fetched))
         print(type(password))
         print(type(passwd))
         '''while(i>=1):
           # print("fetch all works")
            for z in fetched:
               print("db check")
               if passwd == int(z[0]):
                  print("success")
                  i=0
                  cur.close()
                  return render_template("result.html")
               else:
                  print("failure")
                  i=0
                  cur.rollback()
                  cur.close()
                  return render_template("wrongpassword.html")
         '''
         if len(fetched) > 0:
            print("success")
            cur.close()
            return render_template("home.html")
         else:
            print("failure")
            #cur.rollback()
            cur.close()
            return render_template("alarmtrigger.html")
      
         # cur.close()
         return render_template("alarmtrigger.html")

      try:
       #  todayDate = request.form['todayDate']
         password = request.form['password']
         print("password collected")
         with sql.connect("pidatabase.db") as con: 
            print("DB created")
            cur = con.cursor()
            print("Cursor Created")
            cur.execute("SELECT password from userpassword where password = " + password)
            print("Password: " + password)
            print("SQL request taken")
            print("Create temp list to check password")
            print(cur.fetchall())
            fetched = cur.fetchall()
            passwd = int(password)
            #db_check = cur.fetchone()
            print(fetched)
            print(type(fetched))
            print(type(password))
            print(type(passwd))
            '''while(i>=1):
              # print("fetch all works")
               for z in fetched:
                  print("db check")
                  if passwd == int(z[0]):
                     print("success")
                     i=0
                     cur.close()
                     return render_template("result.html")
                  else:
                     print("failure")
                     i=0
                     cur.rollback()
                     cur.close()
                     return render_template("wrongpassword.html")
         '''
            if passwd in fetched[0]:
               print("true")
           # cur.close()
            return render_template("home.html")

      except:
        # con.close()
        # print(post_id)
         print("error")
         return render_template("alarmtrigger.html")
     # finally:
     #    con.close()
       #  return render_template("login.html")
    else:   
      return render_template("alarmtrigger.html")
# main method to run program
# please replace the host with your own pi host IP and can use command below to obtain IP
# replace 127.0.0.1 with what the commnad returns below (IP of Pi)...
# hostname -I
# In browser to access site enter: http://piIP:5000/
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug = True)