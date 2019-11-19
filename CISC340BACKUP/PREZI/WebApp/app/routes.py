import os
import sys
from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/home/:testPATH')
cursor = db.cursor()
    cursor.execute('SELECT * from users)
    row = cursor.fetchone()
    if row:
        return template('hometestPATH', page=row)
    else:
	return render_template('home.html')

@app.route('/checkPassword', methods=['GET','POST')
def checkPassword():
	form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='changePassword', form=form)
