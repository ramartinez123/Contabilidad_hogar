from flask import render_template, request
from flask_login import login_required
from app import app
from DAO.ledgerDao import Queries

def list_by_year(query_function, template_name, default_year=2024):
    try:
        if request.method == "POST":
            ayear = int(request.form['year'])
        else:
            ayear = default_year
        data = query_function(ayear)
        return render_template(template_name, transactions=data)
    except ValueError:
        return render_template(template_name, error="Formato invalido")
    except Exception as e:
        return render_template(template_name, error=str(e))
    
@app.route('/reports/list_looses_byYear', methods=['GET', 'POST'])
@login_required
def list_looses_byYear():
    return list_by_year(Queries.Losses_byYear, "loosesByYear.html")

@app.route('/reports/list_profits_byYear', methods=['GET', 'POST'])
@login_required
def list_profits_byYear():
    return list_by_year(Queries.Profits_byYear, "profitsByYear.html")

@app.route('/reports/list_assets_byYear', methods=['GET', 'POST'])
@login_required
def list_assets_byYear():
    return list_by_year(Queries.Assets_byYear, "assetsByYear.html")

@app.route('/reports/list_assets_byYearD', methods=['GET', 'POST'])
@login_required
def list_assets_byYearD():
    return list_by_year(Queries.Assets_byYear_D, "assetsByYearD.html")

@app.route('/reports/list_liabilities_byYear', methods=['GET', 'POST'])
@login_required
def list_liabilities_byYear():
    return list_by_year(Queries.Liabilities_byYear, "liabilitiesByYear.html")
   

  
