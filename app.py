'''
Quack-a-Moo
Mohammed S. Jamil, Isaac Jon, Ahnaf Kazi, Addison Huang
SoftDev1 pd6
P #00: Da Art of Storytellin'
2018-10-01
'''

from flask import Flask,flash, render_template, request, session, url_for, redirect
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('all.html')

app.debug = True
app.run()
