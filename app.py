'''
Quack-a-Moo
Mohammed S. Jamil, Isaac Jon, Ahnaf Kazi, Addison Huang
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-01
'''
from util import db_updater as update
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
        return render_template('home.html')
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
        return render_template('home.html')
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
        return render_template('all.html')
    else:
        return redirect(url_for("home"))
@app.route("/create",methods=['GET','POST'])
def create():
    if 'username' in session:
        return render_template('create.html')
    else:
        return redirect(url_for("home"))
@app.route("/view",methods=['GET','POST'])
def view():
    if 'username' in session:

        title = request.form["title"] #variables for code readability
        body = request.form["body"]
        username = session["username"]
        #update.create(title, body, username)
        if request.form["submit"] == "create":
            DB_FILE="data/quackamoo.db"
            db = sqlite3.connect(DB_FILE)
            c = db.cursor()
            print(title)
            print(body)
            command = "INSERT INTO stories VALUES(?,?)" #adds the story to the stories db
            params=(title,body)
            c.execute(command, params) #executes the insert story command
            c.execute("SELECT entryId FROM logs") #selects all of the entryids
            entryIds = c.fetchall() #stores the list of entryids as a list
            if len(entryIds) > 0:
                entryId = len(entryIds)#the next entryId in the logs
            else:
                entryId = 0
        command2 = "INSERT INTO logs VALUES(?,?,?,?)" #updates logs
        c.execute(command2, (entryId,username,title,body)) #executes the insert log entry command
        db.commit()
        db.close()
        return render_template('view.html',title=title, story=body)
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
        app.debug = True
        app.run()
