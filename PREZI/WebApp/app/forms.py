import sqlite3 as lite
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

con = lite.connect('database.db')

def create_db():
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (?);", (password)
        cur.commit()

createnewdb = input('Enter 1 to create new db: ')
if createnewdb == 1:
    create_db()
else:
    sys.exit(0)
class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
	submit = SubmitField('changePassword')
