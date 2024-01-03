from flask import render_template, request,redirect,url_for
from flask_login import login_required
from app import app
from DAO.ledgerDao import Queries
   
@app.route('/reports/list_looses_byYear',methods=['GET', 'POST'])
@login_required
def list_looses_byYear():
    if request.method == "POST":
        ayear = int(request.form['year'])
        data= Queries.Losses_byYear(ayear)
        return render_template("loosesByYear.html", transactions = data)
    else:
        data= Queries.Losses_byYear(2024)   
        return render_template("loosesByYear.html", transactions = data)

@app.route('/reports/list_profits_byYear',methods=['GET', 'POST'])
@login_required
def list_profits_byYear():
    if request.method == "POST":
        ayear = int(request.form['year'])
        data= Queries.Profits_byYear(ayear)
        return render_template("profitsByYear.html", transactions = data)
    else:
        data= Queries.Profits_byYear(2024)   
        return render_template("profitsByYear.html", transactions = data)

@app.route('/reports/list_assets_byYear',methods=['GET', 'POST'])
@login_required
def list_assets_byYear():   
    if request.method == "POST":
        ayear = int(request.form['year'])
        data= Queries.Assets_byYear(ayear)
        return render_template("assetsByYear.html", transactions = data)
    else:
        data= Queries.Assets_byYear(2024)   
        return render_template("assetsByYear.html", transactions = data)
    
@app.route('/reports/list_assets_byYearD' ,methods=['GET', 'POST'])
@login_required
def list_assets_byYearD():
    if request.method == "POST":
        ayear = int(request.form['year'])
        data= Queries.Assets_byYear_D(ayear)
        return render_template("assetsByYearD.html", transactions = data)
    else:
        data= Queries.Assets_byYear_D(2024)   
        return render_template("assetsByYearD.html", transactions = data)

@app.route('/reports/list_liabilities_byYear',methods=['GET', 'POST'])
@login_required
def list_liabilities_byYear():
    if request.method == "POST":
        ayear = int(request.form['year'])
        data= Queries.Liabilities_byYear(ayear)
        return render_template("liabilitiesByYear.html", transactions = data)
    else:
        data= Queries.Liabilities_byYear(2024)   
        return render_template("liabilitiesByYear.html", transactions = data)
  
