'''
Team Quack-a-moo
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-17
'''

''' the purpose of this file is a temporary space for the code for populating the logs and users and stories database '''
import sqlite3
DB_FILE = "../data/quackamoo.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor() #facilitates db operations

#when someone creates a story...
if request.form["submit"] == "create": 
    title = request.form["title"] #variables for code readability
    body = request.form["body"]
    username = session["username"]
    command = "INSERT INTO stories VALUES(\"" + title "\"," + body")" #adds the story to the stories db
    c.execute(command) #executes command
    c.execute("SELECT entryId FROM logs") #selects all of the entryids
    entryIds = c.fetchall() #stores the list of entryids as a list
    if len(entryIds) > 0:
        entryId = len(entryIds)#the next entryId in the logs
    else:
        entryId = 0
    command2 = "INSERT INTO logs VALUES(\"" + entryId + "\"," + username + "\"," + title + "\"," + body")" #updates logs


#when some adds to a story...
if request.form["submit"] == "add":
    title = request.form["title"] #variables for code readability
    body = request.form["body"]
    username = session["username"]
    c.execute("SELECT entryId FROM logs") #selects all of the entryids
    entryIds = c.fetchall() #stores the list of entryids as a list
    entryId = len(entryIds)#the next entryId in the logs
    command = "INSERT INTO logs VALUES(\"" + entryId + "\"," + username + "\","+ title + "\"," +body")" #updates logs
    c.execute(command) #executes command
    c.execute("SELECT body FROM stories WHERE stories.title ='" +title + "';")
    oldBody = c.fetchall()
    body = oldBody + body
    command = "UPDATE stories SET body = '" + body + "'WHERE stories.title ='" + title + "';"
    c.execute(command)
    
def adduser(username, password):
    command = "INSERT INTO users VALUES(" + '"' + username + '", "' + password + '")'
    c.execute(command)
    
    
    

    
    
    
    
    

    
    
    



