'''
Team Quack-a-moo
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-17
'''

''' this file stores the updating database code'''

import sqlite3
from flask import request,session
DB_FILE = "./data/quackamoo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor() #facilitates db operations


'''
create()
This function is called when a new story is created
It adds an entry in the logs and stories database
'''
def create(title, body, username):
        DB_FILE="data/quackamoo.db"
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        storyId =  nextStory()
        command = "INSERT INTO stories VALUES(?,?,?)" #adds the story to the stories db
        params=(storyId,title,body)
        c.execute(command, params) #executes the insert story command
        entryId = 0
        command2 = "INSERT INTO logs VALUES(?,?,?,?,?)" #updates logs
        c.execute(command2, (entryId,username,storyId,title,body)) #executes the insert log entry command
        db.commit()
        db.close()

'''
add()
This function is called when someone adds to a story
it adds an entry in the logs and updates the stories database
'''
def add(title,body,username,storyId):
        DB_FILE="data/quackamoo.db"
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        entryId = nextEntry(storyId)    
        insert = "INSERT INTO logs VALUES(?,?,?,?,?)" #updates logs
        c.execute(insert, (entryId,username,storyId,title,body)) #executes the insert log entry command
        get_story="SELECT body FROM stories WHERE stories.title =(?);"
        c.execute(get_story,(title,))
        oldBody = c.fetchone()[0] #stores the old body
        body = oldBody + body #updates the body
        command = "UPDATE stories SET body = (?) WHERE stories.storyId = (?) ;"
        print(command)
        c.execute(command,(body,storyId))
        db.commit()
        db.close()

'''
nextStory()
This function returns the maximum storyId + 1
'''
def nextStory():
        DB_FILE="data/quackamoo.db"
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("SELECT storyId FROM stories") #selects all of the entryids
        storyIds = c.fetchall() #stores the list of entryids as a list
        if len(storyIds) > 0:
                storyId = len(storyIds)#the next entryId in the logs
        else:
                storyId = 0
        return storyId

'''
nextEntry()
This function returns the maximum entryId + 1
'''
def nextEntry(storyId):
        DB_FILE="data/quackamoo.db"
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        select="SELECT entryId FROM logs WHERE logs.storyId=(?)"
        c.execute(select,(storyId,)) #selects all of the entryids
        entryIds = c.fetchall() #stores the list of entryids as a list
        if len(entryIds) > 0:
                entryId = len(entryIds)#the next entryId in the logs
        else:
                entryId = 0
        return entryId
        
    
    

    
    
    
    
    

    
    
    



