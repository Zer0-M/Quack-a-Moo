'''
JamBuds
Sophia Xia, Mohammed S. Jamil
SoftDev1 pd6
K15 -- Oh yes, perhaps I do...
2018-10-01
'''

from flask import Flask,flash, render_template, request, session, url_for, redirect
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO"

app.debug = True
app.run()
