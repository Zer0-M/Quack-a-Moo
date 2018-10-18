##IsaacWuton -- Jeffrey Wu and Isaac Jon
##SoftDev1 pd6
##K15 - Oh yes, perhaps I do...
##2018-10-02

from flask import Flask,render_template,request,session,url_for,redirect,flash
from os import urandom

app = Flask(__name__)
username = 'zero123'
password = '1234'
app.secret_key = urandom(32)

@app.route("/")
def home():
    if 'username' in session:
        return render_template('welcome.html', u = username)
    else:
        return render_template('home.html')

@app.route("/auth")
def authPage():        
    if request.args['username'] != username:
        flash('username incorrect')
        if (request.args['password'] != password):
            flash('password incorrect')
        return redirect(url_for('home'))
    elif request.args['username'] == username: 
        if request.args['password'] == password:
            session['username'] = username
            return render_template('welcome.html', u = username, message = "Welcome ", x = "Logout")
        else:
            flash('password incorrect')
            return redirect(url_for('home'))

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("home"))
if __name__ == '__main__':
        app.debug = True
        app.run()
