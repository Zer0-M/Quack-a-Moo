def create():
    if request.form["submit"] == "create": 
        title = request.form["title"] #variables for code readability
        body = request.form["body"]
        username = session["username"]
        command = "INSERT INTO stories VALUES(\"" + title "\"," + body")" #adds the story to the stories db
        c.execute(command) #executes the insert story command
        print("Stories entry - title: " + title + "|body: " + body)
        c.execute("SELECT entryId FROM logs") #selects all of the entryids
        entryIds = c.fetchall() #stores the list of entryids as a list
        if len(entryIds) > 0:
            entryId = len(entryIds)#the next entryId in the logs
        else:
            entryId = 0
        command2 = "INSERT INTO logs VALUES(\"" + entryId + "\"," + username + "\"," + title + "\"," + body")" #updates logs
        c.execute(command2) #executes the insert log entry command
        print("Log entry - ID: " + entryId + " |username: " + username + "|title: " + title + "|text: " + body)
