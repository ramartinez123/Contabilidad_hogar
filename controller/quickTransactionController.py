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
        transaction1 = Transactions(
            "",
            request.form['actividad1'],
            0,
            1,
            request.form['to_day'],
            request.form['feeQuickInsert1'],
            1,
            1,
            "",
            0
        )
        transaction2 = Transactions(
            "",
            request.form['medio1'],
            0,
            2,
            request.form['to_day'],
            request.form['feeQuickInsert1'],
            1,
            1,
            "",
            0
        )

       
        Queries.InsertQuickTransac(transaction1) 
        Queries.InsertQuickTransac(transaction2)
        return redirect(url_for("quickinsert"))