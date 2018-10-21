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
        return render_template('home.html', u = username)
    else:
        return render_template('auth.html')

@app.route("/auth",methods=['GET','POST'])
def authPage():        
    if request.form['username'] != username:
        flash('incorrect credentials')
        return redirect(url_for('home'))
    elif request.form['username'] == username: 
        if request.form['password'] == password:
            session['username'] = username
            return render_template('home.html', u=username)
        else:
            flash('incorrect credentials')
            return redirect(url_for('home'))

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("home"))
@app.route("/all")
def all():
    if 'username' in session:
        return render_template('all.html', u = username)
    else:
        return redirect(url_for("home"))
@app.route("/create",methods=['GET','POST'])
def create():
    if 'username' in session:
        return render_template('create.html', u = username)
    else:
        return redirect(url_for("home"))
@app.route("/view",methods=['GET','POST'])
def view():
    if 'username' in session:
        name=request.form['title']
        text=request.form['story']
        print(name)
        return render_template('view.html',title=name, story=text)
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
        app.debug = True
        app.run()

