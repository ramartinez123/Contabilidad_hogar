from flask import render_template
from app import app, mysql

@app.route('/home')
def index(): 
    return render_template("index.html") 

