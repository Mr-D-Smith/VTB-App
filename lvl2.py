from flask import Flask,session,redirect,url_for,request,render_template
import sqlite3
import os
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)  

def get_flag():
    random_bytes = os.urandom(12)
    flag = "CTF{" + base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=') + "}"
    with open('.flag.txt','w') as file:
        file.write(flag)
    return flag
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
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if check_creds(username,password):
            session['logged_in']=True
            session['username']=username
            return redirect(url_for('dashboard'))
        return render_template("login.html")
    return render_template('login.html',error=None)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('result.html',success=True,message=f"Welcome {session['username']}",flag=get_flag())


if __name__== "__main__":
    app.run(debug=True)