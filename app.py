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
from util import db_builder as builder
from passlib.hash import sha256_crypt

import sqlite3 #imports sqlite
app = Flask(__name__)
app.secret_key = urandom(32)

builder.main()
'''
every page has a home and logout button
'''
'''
homepage
1) edited stories
2) all stories
3) most popular stories
4) create a story
'''
@app.route("/")
def home():
    if 'username' in session: #if user is logged in
        if "logoutbutton" in request.args: #if user logs out
            session.pop('username')
            return redirect(url_for('home'))
        username = session['username']
        editedList = search.edited(username)
        most=[]
        return render_template('home.html',edited=editedList, popular=most)
    else:
        return render_template('auth.html')

'''
authPage
checks if the users credentials matches the credentials in the database
'''
@app.route("/auth",methods=['GET','POST'])
def authPage():
    username=request.form['username'] #username
    password = search.password(username) #password that matches the username
    if password == None: #if credentials are incorrect
        flash('incorrect credentials')
        return redirect(url_for('home')) #redirects
    elif sha256_crypt.verify(request.form['password'], password[0]): #if password is correct, login
        session['username'] = username
        editedList = search.edited(username)
        most=[]
        return render_template('home.html',edited=editedList, popular=most)
    else: #else credentials are wrong
        flash('incorrect credentials')
        return redirect(url_for('home'))

'''
reg
this page is where the user registers for an account
'''
@app.route("/reg",methods=['GET','POST'])
def reg():
    return render_template('reg.html')

'''
added
adds the users credentials to the database
'''
@app.route("/added",methods=['GET','POST'])
def added():
    newUsername = request.form['username']
    newPassword = sha256_crypt.encrypt(request.form['password']) #encrypts password
    userList = search.username(newUsername)
    if userList == [] : #if username isn't taken
        update.adduser(newUsername,newPassword) #add to database
        return redirect(url_for('home'))
    else: #if username is taken
        flash('Username Taken')
        return redirect(url_for('reg'))

'''
all
this page has a link to every story
'''
@app.route("/all")
def all():
    if 'username' in session:
        storylist=search.all() #retrieves all of the stories
        return render_template('all.html',storylist=storylist)
    else:
        return redirect(url_for("home"))

'''
create
this page is where the user can create a story
'''
@app.route("/create",methods=['GET','POST'])
def create():
    if 'username' in session:
        return render_template('create.html')
    else:
        return redirect(url_for("home"))

'''
view
this page is where the user gets to see a story that they edited
'''
@app.route("/view",methods=['GET','POST'])
def view():
    if 'username' in session:
        #variables for code readability
        username = session["username"]
        if request.referrer == "http://127.0.0.1:5000/create": #if a user created a story
            title = request.form["title"]
            body = request.form["body"]
            update.create(title, body, username) #adds the story to logs and stories
        else: #if the user added to a story or is viewing it
            title = request.args["title"]
            storyId= request.args["storyId"]
            if "submit" in request.form: #if the user added to the story
                body=request.form["body"]
                update.add(title,body,username,storyId) #adds the story to logs and updated the body in stories
            body=search.body(storyId) #retrieves the body of the story
        return render_template('view.html',title=title, story=body)
    else:
        return redirect(url_for("home"))

'''
edit
this is the edit page when adding to a story
'''
@app.route("/edit",methods=['GET','POST'])
def edit():
    if 'username' in session:
        title=request.args["title"] #variables for code readbility
        storyId = request.args["storyId"]
        username = session["username"]
        edit=search.edit(username,storyId)#this variable is used to check if a user has edited a story, if its empty the user has not edited it
        if edit != None : #if user already edited
            flash("Already edited. View from home page")
            return redirect(url_for("home"))
        body=search.text(storyId)
        return render_template('edit.html',title=title, story=body, storyId = storyId)
    else:
        return redirect(url_for("home"))

'''
search
this is the page when you search for a story
'''
@app.route("/search")
def s():
    s = request.args["search_story"]
    l = []
    for title in search.searchresults(s):
        l.append(title[0])
    return render_template('search.html',stories=l)

if __name__ == '__main__':
    app.debug = True
    app.run()
