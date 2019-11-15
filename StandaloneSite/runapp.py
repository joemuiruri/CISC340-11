import datetime
import sys
import os
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
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('password.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         todayDate = request.form['todayDate']
         password = request.form['password']
         
         with sql.connect("pidatabase.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO userpassword (todayDate,password) VALUES (?,?)",(todayDate,password) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("pidatabase.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("SELECT * FROM userpassword")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    password = request.form["password"]  
    with sql.connect("pidatabase.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from userpassword where password = ?",password)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  

@app.route('/login')
def login():
      try:
         
         
         with sql.connect("pidatabase.db") as con:
            password = request.form['password']
            cur = con.cursor()
            
            cur.execute("SELECT password from userpassword where password =?",password)
            
            con.commit()
            msg = "Able to login"
            return render_template("result.html")
      except:
         con.rollback()
         return render_template("gpiopage.html")

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
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug = True)