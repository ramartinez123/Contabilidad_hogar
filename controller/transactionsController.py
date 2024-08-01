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

    try:
        # Crear la primera transacción
        transaction1 = Transactions(
            "", 
            request.form['accounts1'], 
            request.form['subaccountForm'], 
            request.form['debeHaberForm'], 
            request.form['dateForm'], 
            request.form['feeForm'], 
            request.form['countryForm'], 
            request.form['districtForm'], 
            request.form['commentForm'], 
            request.form['cuotaForm']
        )

        # Crear la segunda transacción
        transaction2 = Transactions(
            "", 
            request.form['accounts2'], 
            request.form['subaccountForm2'], 
            request.form['debeHaberForm2'], 
            request.form['dateForm'], 
            request.form['feeForm'], 
            request.form['countryForm'], 
            request.form['districtForm'], 
            request.form['commentForm'], 
            request.form['cuotaForm']
        )

        # Insertar transacciones
        Queries.InsertTransaction(transaction1)
        Queries.InsertTransaction(transaction2)

        return redirect(url_for("transactions"))
    
    except Exception as e:
        print(f"Error al insertar transacciones: {e}")
        return redirect(url_for("transactions"))
   
@app.route('/transactions/list_transactions')
@login_required
def list_transactions():
    try:
        data= Queries.QueryTransaction()
        return render_template("transactions.html", transactions = data)
    except Exception as e:
        print(f"Error al listar transacciones: {e}")
        return render_template("error.html", error_message="No se pudieron recuperar las transacciones.")
    
@app.route('/transactions/update_exchange_t')
@login_required
def update_exchange_t():
    try:
        Queries.InsertExchange()
        return redirect(url_for("list_assets_byYear"))
    except Exception as e:
        print(f"Error al actualizar el intercambio: {e}")
        return redirect(url_for("list_assets_byYear"))

@app.route('/transactions')
@login_required
def transactions(): 
    try:
        current_time=datetime.now().strftime("%Y-%m-%d")
        data=QueriesAccount.QueryAccountNames()
        data1=QueriesAccount.QueryAccountCountries()
        data2=QueriesAccount.QueryAccountCities()
        return render_template("insertTransactions.html", to_day = current_time, accountName=data,countryName=data1,cityName=data2) 
    except Exception as e:
        print(f"Error al cargar la página de transacciones: {e}")
        return render_template("error.html", error_message="No se pudieron cargar los datos")
                               
@app.cli.command()
def test():
    tests= unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.route('/transactions/list_transactions_byDate/<theDate>')
def list_transactions_byDate(theDate):
    thedate = Transactions ("","","","",theDate,"","","","","")
    data= Queries.QuerybyDate(theDate)
    return render_template("transactionsByDate.html", transactions = data) 



    
