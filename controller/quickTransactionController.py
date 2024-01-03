from flask import render_template,request,redirect,url_for
from flask_login import login_required
from app import app
from DAO.quickDao import Queries
from models.transactions import Transactions
from datetime import datetime
 
@app.route('/quickinsert')
@login_required
def quickinsert(): 
    current_time=datetime.now().strftime("%Y-%m-%d")
    return render_template("quickinsert.html", to_day = current_time) 

@app.route('/transactions/quickinserta', methods=['POST'])
def quickinserta():
    if request.method == "POST":
        transaction_account = request.form['actividad1']
        transaction_subaccount = 0
        transaction_date =request.form['to_day']
        transaction_amount = request.form['feeQuickInsert1']
        transaction_increased = 1
        transaction_country = 1
        transaction_city = 1
        transaction_quote = 0
        transaction_comment = ""

        transaction = Transactions ("",transaction_account,transaction_subaccount,transaction_increased
                                      ,transaction_date,transaction_amount,transaction_country
                                      ,transaction_city,transaction_comment,transaction_quote)
        
        transaction_account2 = request.form['medio1']
        transaction_subaccount2 = 0      
        transaction_date2 = request.form['to_day']
        transaction_amount2 = request.form['feeQuickInsert1']
        transaction_increased2 = 2
        transaction_country2 = 1
        transaction_city2 = 1
        transaction_quote2 = 0
        transaction_comment2 = ""


        transaction2 = Transactions ("",transaction_account2,transaction_subaccount2,transaction_increased2
                                      ,transaction_date2,transaction_amount2,transaction_country2
                                      ,transaction_city2,transaction_comment2,transaction_quote2)
        
        Queries.InsertQuickTransac(transaction) 
        Queries.InsertQuickTransac(transaction2)
        return redirect(url_for("quickinsert"))