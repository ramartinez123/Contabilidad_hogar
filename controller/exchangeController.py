from flask import render_template,request,redirect,url_for
from flask_login import login_required
from app import app
from DAO.exchangeDao import Exchanges
from models.exchange import Exchange
from datetime import datetime

@app.route('/exchange')
@login_required
def exchange(): 
    current_time=datetime.now().strftime("%Y-%m-%d")
    return render_template("compCotiz.html", to_day = current_time) 

@app.route('/exchange/insertExchange', methods=['POST'])
@login_required
def insertExchange():
    if request.method == "POST":
        transaction_date =request.form['to_day']
        transaction_amount = request.form['cotiz1']
        transaction_currency = request.form['currency']
        transaction = Exchange ("",transaction_date,transaction_currency,transaction_amount)
        Exchanges.InsertExchange(transaction) 
        return redirect(url_for("exchange"))
    
@app.route('/cotiz/listExchange')
@login_required
def listExchange():
    data= Exchanges.QueryExchange()
    return render_template("cotiz.html", transactions = data)


    
