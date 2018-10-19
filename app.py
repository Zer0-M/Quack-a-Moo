'''
Quack-a-Moo
Mohammed S. Jamil, Isaac Jon, Ahnaf Kazi, Addison Huang
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-01
'''

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
        return render_template('auth.html')

@app.route("/auth")
def authPage():        
    if request.forms['username'] != username:
        flash('username incorrect')
        if (request.forms['password'] != password):
            flash('password incorrect')
        return redirect(url_for('home'))
    elif request.forms['username'] == username: 
        if request.forms['password'] == password:
            session['username'] = username
            return render_template('home.html',name = username)
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

