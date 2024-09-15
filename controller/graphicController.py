from flask import render_template
from flask_login import login_required
from app import app
from DAO.graphicsDao import *
   
@app.route('/graphics')
@login_required
def graphics():
    data= Queries.LossesGraphic()
    datas= Queries.AssetsGraphics()
    datas2=Queries.Losses_byGraphic()
    datas3=Queries.LiabilitiesGraphics()
    datas4=Queries.dolar_cotiz()
    return render_template("graphics.html", transactions = data, assets = datas, categories=datas2, liability=datas3, dollar=datas4)


