from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def unUnauthorized(e):
    return render_template('401.html'), 401



