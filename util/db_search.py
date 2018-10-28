'''
Team Quack-a-moo
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-17
'''

''' this file stores the searching through a database code'''

import sqlite3
from flask import request,session

'''
body(storyId)
returns the body of the story that matches the storyId number
'''
def body(storyId):
    DB_FILE = "./data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = 'SELECT body FROM stories WHERE stories.storyId = "{0}";'.format(storyId)
    c.execute(command)
    body=c.fetchone()[0]
    return body

'''
edited(username)
returns a list of stories that were edited by the user
'''
def edited(username):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    command = 'SELECT storyId,title FROM logs WHERE logs.username = "{0}";'.format(username)
    c.execute(command)
    editedList = c.fetchall()
    return editedList

'''
password(username)
returns the password that matches the username if one exists
else return none
'''
def password(username):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    command = 'SELECT password FROM users WHERE users.username = "{0}"'.format(username)
    c.execute(command)
    password = c.fetchone()
    return password

'''
username(username)
returns an empty list if username doesn't exist in the database
returns [username] if username exists
'''
def username(username):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() 
    command = 'SELECT username FROM users WHERE users.username = "{0}";'.format(username)
    c.execute(command)
    userList = c.fetchall()
    return userList

'''
edit(username,storyId)
returns an empty list if user did not edit the story
returns a not empty list if user edited the story
'''
def edit(username,storyId):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() 
    check="SELECT storyId FROM logs WHERE username = (?) AND storyId=(?);"
    c.execute(check,(username,storyId))
    edit=c.fetchone()
    return edit

'''
text(storyId)
returns the last addition to the story
'''

def text(storyId):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    command =  "SELECT entryId FROM logs WHERE storyId = (?)" #selects all of the entryids
    c.execute(command,storyId)
    entryIds = c.fetchall()
    last=entryIds[len(entryIds)-1][0]
    command2 = 'SELECT body FROM logs WHERE entryId = (?);'
    c.execute(command2,[str(last)])
    text=c.fetchone()[0]
    return text
