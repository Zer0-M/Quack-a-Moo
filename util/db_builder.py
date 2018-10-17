'''
Team Quack-a-moo
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-17
'''

import sqlite3 #imports sqlite

DB_FILE="../data/quackamoo.db" 

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor() #facilitates db operations

def users(): #creates the users db
    command = "CREATE TABLE users(username TEXT, password TEXT, userId INTEGER)"
    c.execute(command)

def story(): #create the story db
    command = "CREATE TABLE stories(storyId INTEGER, title TEXT, body TEXT)"
    c.execute(command)

def logs(): #creates the logs db
    command = "CREATE TABLE logs(entryId INTEGER, storyId INTEGER, userId INTEGER, text TEXT)"
    c.execute(command)

def main(): #calls all of the functions to build the databases
    users()
    story()
    logs()

main()
