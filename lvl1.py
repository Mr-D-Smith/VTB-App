from flask import Flask,request,render_template
import base64
import os
import sqlite3
app = Flask(__name__)

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
            return render_template('result.html', success=True, message='Welcome back!', flag=get_flag())
        return render_template("result.html", success=False,message="Login Failed")
    return render_template('login.html',error=None)


if __name__== "__main__":
    app.run(debug=True)