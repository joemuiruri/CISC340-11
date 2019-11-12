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
      return redirect(url_for('index'))

@app.route('/home')
def index():
    user = {'username': 'team11'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home.html', title='Home', user=user, posts=posts)


