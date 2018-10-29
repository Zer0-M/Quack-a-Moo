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
    get_stories = 'SELECT body FROM stories WHERE stories.storyId = (?);'
    c.execute(get_stories,(storyId,))
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
    list_stories = 'SELECT storyId,title FROM logs WHERE logs.username = (?) ORDER BY title;'
    c.execute(list_stories,(username,))
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
    get_password = 'SELECT password FROM users WHERE users.username = (?)'
    c.execute(get_password,(username,))
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
    user_exists = 'SELECT username FROM users WHERE users.username = (?);'
    c.execute(user_exists,(username,))
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
    get_story = 'SELECT body FROM logs WHERE storyId = (?) ORDER BY entryId DESC;'
    c.execute(get_story,(storyId,))
    text=c.fetchone()[0]
    return text

'''
all()
returns a list of all of the stories
'''
def all():
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    getstories="SELECT title,storyId FROM stories"
    c.execute(getstories)
    storylist=c.fetchall()
    return storylist

'''
best()
returns a the top 3 stories based on the number of edits
'''
def best():
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    top_3 = 'SELECT entryId,storyId,title FROM logs GROUP BY storyId ORDER BY entryId DESC LIMIT 0,3;'#GROUP BY removes duplicates, LIMIT makes sure the top 3 stories are displayed
    c.execute(top_3)
    most = []
    temp = c.fetchall()
    i=0
    while i<3:
        most.append(temp[i])
        i=i+1
    return most

'''
searchresults(s)
returns list of stories that contain s
'''
def searchresults(s):
    DB_FILE="data/quackamoo.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    get = "SELECT title,storyId FROM stories WHERE title LIKE " + "'%" + s + "%'"
    c.execute(get)
    list = c.fetchall()
    return list
