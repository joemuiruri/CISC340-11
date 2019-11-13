import os
import sys

from flask import Flask, flash, redirect, render_template, request, session, abort
from app import app

@app.route('/home')
def home():
	return render_template('home.html', title='Home')
@app.route('/index')
def index():
	return render_template('index.html', title='Profile')
@app.route('/changePassword')
def change_password():
	return render_template('login.html', title='Reset')
