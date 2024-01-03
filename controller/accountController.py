from flask import render_template
from flask_login import login_required
from app import app
from DAO.accountDAO import QueriesAccount

    
@app.route('/account/listAccount') 
@login_required 
def listAccount():
    data= QueriesAccount.QueryAccount()
    return render_template("account.html", accounts = data)



