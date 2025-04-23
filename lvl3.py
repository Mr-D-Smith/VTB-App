from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
import sqlite3
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)
csrf = CSRFProtect(app)

def get_flag():
    random_bytes = os.urandom(12)
    flag = "CTF{" + base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=') + "}"
    with open('.flag.txt','w') as file:
        file.write(flag)
    return flag
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

def check_creds(username,password):
    conn=sqlite3.Connection('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    result = cursor.fetchone()

    conn.close()
    return result is not None
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username=form.username.data.strip()
        password=form.password.data.strip()
        if check_creds(username,password):
            session['username']=username
            session['logged_in']=True
            return redirect(url_for('dashboard'))
        return render_template("login3.html",form=form)
    return render_template("login3.html",form=form)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('result.html',success=True,message=f"Welcome {session['username']}",flag=get_flag())


if __name__== "__main__":
    app.run(debug=True)