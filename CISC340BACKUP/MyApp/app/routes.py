from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/index')
def testpage():
   return render_template('index.html',title='IndexPage')

@app.route('/login', methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      flash('Login requested for username={}, remember_me={}'.format(form.username.data, form.remember_me.data))
      return redirect('/home')
   return render_template('login.html', title='Sign In', form=form)

@app.route('/home')
def index():
    user = {'username': 'team11'}
    posts = [
        {
            'author': {'username': 'team11'},
            'body': '1234'
        },
        {
            'author': {'username': 'team11-encry'},
            'body': '_X1234X_'
        }
    ]
    return render_template('home.html', title='Home', user=user, posts=posts)


