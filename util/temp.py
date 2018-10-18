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

#when someone adds a story...
if request.form["submit"] == "add": 
    title = request.form["title"] #variables for code readability
    body = request.form["body"]
    username = session["username"]
    command = "INSERT INTO stories VALUES(\"" + title "\"," + body")" #adds the story to the stories db
    c.execute(command) #executes command
    
    
    
    

    
    
    



