'''
Quack-a-Moo
Mohammed S. Jamil, Isaac Jon, Ahnaf Kazi, Addison Huang
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-01
'''

from flask import Flask,render_template,request,session,url_for,redirect,flash
from os import urandom

import sqlite3 #imports sqlite
DB_FILE="data/quackamoo.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor() #facilitates db operations

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/")
def home():
    if 'username' in session:
        return render_template('home.html', u = username)
    else:
        return render_template('auth.html')

@app.route("/auth",methods=['GET','POST'])
def authPage():
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() 
    username=request.form['username']
    command = 'SELECT password FROM users WHERE users.username = "{0}"'.format(username)
    c.execute(command)
    password = c.fetchone()
    print(password[0])
    if password == []:
        flash('incorrect credentials')
        return redirect(url_for('home'))
    elif request.form['password'] == password[0]:
        session['username'] = username
        return render_template('home.html', u=username)
    else:
        flash('incorrect credentials')
        return redirect(url_for('home'))
@app.route("/reg",methods=['GET','POST'])
def reg():
    return render_template('reg.html')
@app.route("/added",methods=['GET','POST'])
def added():
    DB_FILE="data/quackamoo.db"
    newUsername = request.form['username']
    newPassword = request.form['password']
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() 
    command = 'SELECT username FROM users;'
    c.execute(command)
    userList = c.fetchall()
    print(userList)
    if newUsername not in userList:
        insert = "INSERT INTO users VALUES(?,?)"
        params=(newUsername,newPassword)
        c.execute(insert,params)
        db.commit()
        db.close()
        #session['username'] = newUsername
        return redirect(url_for('home'))
    else:
        flash('Username Taken')
        return redirect(url_for('home'))


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("home"))
@app.route("/all")
def all():
    if 'username' in session:
        return render_template('all.html', u = username)
    else:
        return redirect(url_for("home"))
@app.route("/create",methods=['GET','POST'])
def create():
    if 'username' in session:
        return render_template('create.html', u = username)
    else:
        return redirect(url_for("home"))
@app.route("/view",methods=['GET','POST'])
def view():
    if 'username' in session:
        name=request.form['title']
        text=request.form['story']
        print(name)
        return render_template('view.html',title=name, story=text)
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
        app.debug = True
        app.run()
