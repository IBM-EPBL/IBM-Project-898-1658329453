# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:07:32 2022

@author: Kavin
"""

from flask import Flask, render_template 
app = Flask(__name__ )
@app.route('/', methods =["GET", "POST"]) 
def Index():
 return render_template('index.html') 
@app.route('/Blog') 
def Blog():
 return render_template('blog.html') 
@app.route('/Signup')
def Signup():
 return render_template('signup.html') 
@app.route('/Signin')
def Signin():
 return render_template('signin.html') 
if __name__ =='__main__':
 app.debug = True
 app.run()
