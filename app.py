'''
Quack-a-Moo
Mohammed S. Jamil, Isaac Jon, Ahnaf Kazi, Addison Huang
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-01
'''
from flask import Flask,render_template,request,session,url_for,redirect,flash
from os import urandom
from util import db_updater as update
from util import db_search as search
from passlib.hash import sha256_crypt

import sqlite3 #imports sqlite
app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/")
def home():
    if 'username' in session:
        if "logoutbutton" in request.args:
            session.pop('username')
            return redirect(url_for('home'))
        username = session['username']
        editedList = search.edited(username)
        most=[]
        return render_template('home.html',edited=editedList, popular=most)
    else:
        return render_template('auth.html')

@app.route("/auth",methods=['GET','POST'])
def authPage():
    username=request.form['username']
    password = search.password(username)
    if password == None:
        flash('incorrect credentials')
        return redirect(url_for('home'))
    elif sha256_crypt.verify(request.form['password'], password[0]):
        session['username'] = username
        editedList = search.edited(username)
        most=[]
        return render_template('home.html',edited=editedList, popular=most)
    else:
        flash('incorrect credentials')
        return redirect(url_for('home'))
    
@app.route("/reg",methods=['GET','POST'])
def reg():
    return render_template('reg.html')

@app.route("/added",methods=['GET','POST'])
def added():
    newUsername = request.form['username']
    newPassword = sha256_crypt.encrypt(request.form['password'])
    userList = search.username(newUsername)
    print(userList)
    if userList == [] :
        update.adduser(newUsername,newPassword)
        return redirect(url_for('home'))
    else:
        flash('Username Taken')
        return redirect(url_for('reg'))

@app.route("/all")
def all():
    if 'username' in session:
        storylist=search.all()
        return render_template('all.html',storylist=storylist)
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
        #variables for code readability
        username = session["username"]
        if request.referrer == "http://127.0.0.1:5000/create":
            title = request.form["title"]
            body = request.form["body"]
            update.create(title, body, username)
        else:
            title = request.args["title"]
            storyId= request.args["storyId"] 
            if "submit" in request.form:
                body=request.form["body"]
                update.add(title,body,username,storyId) 
            body=search.body(storyId)
        return render_template('view.html',title=title, story=body)
    else:
        return redirect(url_for("home"))
    
@app.route("/edit",methods=['GET','POST'])
def edit():
    if 'username' in session:
        title=request.args["title"]
        storyId = request.args["storyId"]
        username = session["username"]
        edit=search.edit(username,storyId)#this variable is used to check if a user has edited a story, if its empty the user has not edited it
        if edit != None :
            flash("Already edited. View from home page")
            return redirect(url_for("home"))
        body=search.text(storyId)
        return render_template('edit.html',title=title, story=body, storyId = storyId)
    else:
        return redirect(url_for("home"))
if __name__ == '__main__':
    app.debug = True
    app.run()
