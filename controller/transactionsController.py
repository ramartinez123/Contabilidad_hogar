from flask import render_template,request,redirect,url_for
from flask_login import login_required
from app import app
from DAO.transactionsDao import Queries
from models.transactions import Transactions
from DAO.accountDAO import QueriesAccount
from datetime import datetime
import unittest

@app.route('/transactions/insert_transactions', methods=['POST'])
@login_required
def insert_transactions():
    if request.method == "POST":
        transaction_account = request.form['accounts1']
        transaction_subaccount = request.form['subaccountForm']
        transaction_date = request.form['dateForm']
        transaction_amount = request.form['feeForm']
        transaction_increased = request.form['debeHaberForm']
        transaction_country = request.form['countryForm']
        transaction_city = request.form['districtForm']
        transaction_quote = request.form['cuotaForm']
        transaction_comment = request.form['commentForm']

        transaction = Transactions ("",transaction_account,transaction_subaccount,transaction_increased
                                      ,transaction_date,transaction_amount,transaction_country
                                      ,transaction_city,transaction_comment,transaction_quote)
        

        transaction_account2 = request.form['accounts2']
        transaction_subaccount2 = request.form['subaccountForm2']       
        transaction_date2 = request.form['dateForm']
        transaction_amount2 = request.form['feeForm']
        transaction_increased2 = request.form['debeHaberForm2']
        transaction_country2 = request.form['countryForm']
        transaction_city2 = request.form['districtForm']
        transaction_quote2 = request.form['cuotaForm']
        transaction_comment2 = request.form['commentForm']


        transaction2 = Transactions ("",transaction_account2,transaction_subaccount2,transaction_increased2
                                      ,transaction_date2,transaction_amount2,transaction_country2
                                      ,transaction_city2,transaction_comment2,transaction_quote2)

        Queries.InsertTransaction(transaction) 
        Queries.InsertTransaction(transaction2)
        return redirect(url_for("transactions"))
    
@app.route('/transactions/list_transactions')
@login_required
def list_transactions():
    data= Queries.QueryTransaction()
    return render_template("transactions.html", transactions = data)

@app.route('/transactions/update_exchange_t')
@login_required
def update_exchange_t():
    Queries.InsertExchange()
    return redirect(url_for("list_assets_byYear"))

@app.route('/transactions')
@login_required
def transactions(): 
    current_time=datetime.now().strftime("%Y-%m-%d")
    data=QueriesAccount.QueryAccountNames()
    data1=QueriesAccount.QueryAccountCountries()
    data2=QueriesAccount.QueryAccountCities()
    return render_template("insertTransactions.html", to_day = current_time, accountName=data,countryName=data1,cityName=data2) 

@app.cli.command()
def test():
    tests= unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

#aca estoy 
@app.route('/transactions/list_transactions_byDate/<theDate>')
def list_transactions_byDate(theDate):
    thedate = Transactions ("","","","",theDate,"","","","","")
    data= Queries.QuerybyDate(theDate)
    return render_template("transactionsByDate.html", transactions = data) 



    
