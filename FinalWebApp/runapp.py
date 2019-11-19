# Team 11
# CISC 340 - Term Project
# This python script runs our web application and to start the app please..
#  1. check python update (We are using python 2.7)
#  2. Start virtual environment... source venv/scripts/activate || python venv/scripts/activate_this.py
#  3. Create database... python createdb.py || python3 createdb.py
#  4. Start WebApp... python runapp.py || python3 runapp.py
#  5. Please see our Github and download our lateest C program
import datetime
import sys
import os
import time
import serial
import gpout
from flask import Flask, redirect,url_for, abort, render_template, request
from jinja2 import Environment, PackageLoader 
import sqlite3 as sql
#import RPi.GPIO as GPIO
app = Flask(__name__)
# Start of web app
@app.route('/')
def home():
   print("print test")
   gpout.deactivateAlarm()
   return render_template('home.html')
@app.route('/sensortrigger')
def sensortrigger():
    render_template("sensortrigger.html")
    return redirect(url_for("result"))
# Method to check User Password vs Database password... 
# If passwords don't match, trigger the alarm  
@app.route('/login',methods = ['POST','GET'])
def login():
    i=1
    if request.method == 'POST':
      password = request.form['password']
      print("password collected")
      with sql.connect("pidatabase.db") as con:
         print("DB created")
         cur = con.cursor()
         print("Cursor Created")
         cur.execute("SELECT password FROM userpassword WHERE password = " + password)
         # Comments were mainly used for debugging 
         #print("Password: " + password)
         #print("SQL request taken")
         #print("Create temp list to check password")
         #print(cur.fetchall())
         fetched = cur.fetchall()
         passwd = int(password)
         # Comments were mainly used for debugging 
         # print(fetched)
         # print(type(fetched))
         # print(type(password))
         # print(type(passwd))
         if len(fetched) > 0:
            print("success")
            cur.close()
            # render_with_context("sensortrigger.html")
            # Take Advantage of Flask redirect feature!
            return redirect(url_for("sensortrigger"))
         else:
            print("failure")
            cur.close()
            return redirect(url_for("login"))
    else:   
      return render_template("login.html")
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
      password = request.form['password']
      print("password collected")
      with sql.connect("pidatabase.db") as con: 
         print("DB created")
         cur = con.cursor()
         print("Cursor Created")
         cur.execute("SELECT password from userpassword where password = " + password)
         #print("Password: " + password)
         #print("SQL request taken")
         #print("Create temp list to check password")
         #print(cur.fetchall())
         fetched = cur.fetchall()
         passwd = int(password)
         #print(fetched)
         #rint(type(fetched))
         #print(type(password))
         #print(type(passwd))
         if len(fetched) > 0:
            print("success")
            cur.close()
            gpout.deactivateAlarm()
            return render_template("home.html")
         else:
            print("failure")
            #cur.rollback()
            cur.close()
            return render_template("alarmtrigger.html")
         # cur.close()
         return render_template("alarmtrigger.html")
    else:   
      return render_template("alarmtrigger.html")
# GPIO funtion that controls the data sent to Basys3
@app.route('/result')
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
      print(processedins)
      if(processedins == '1'):
         print("triggered")
         return render_template("alarmtrigger.html")
# Extra Features
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

# Update Database by adding new password
@app.route('/enternew')
def newuser():
   return render_template('password.html')
# Method to connect to our db (pidatabase) and add a password with the current date 
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         password = request.form['password']
         # Start DB connection
         with sql.connect("pidatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO userpassword (password) VALUES (?)",(password) )     
            con.commit()
            msg = "Record successfully added"
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
   cur.execute("SELECT id, password FROM userpassword")  
   rows = cur.fetchall()
   con.close()
   return render_template("list.html",rows = rows)
   
# Set button and PIR sensor pins as an input
#GPIO.setup(button, GPIO.IN)   
#GPIO.setup(senPIR, GPIO.IN)
# main method to run program
# please replace the host with your own pi host IP and can use command below to obtain IP
# replace 127.0.0.1 with what the commnad returns below (IP of Pi)...
# hostname -I
# In browser to access site enter: http://piIP:5000/
if __name__ == '__main__':
   app.run(host='192.168.0.133',debug = True)


   # Extra notes 
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
