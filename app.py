# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")
    #return "Hello World!"
    
@app.route("/assignments")
def secondWebpage():
    return render_template("assignments.html")

@app.route("/classes")
def lastWebpage():
    return render_template("classes.html")


#start the server
if __name__ == "__main__":
    app.run()