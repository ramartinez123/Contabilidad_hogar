from flask_testing import TestCase
from flask import current_app
from app import app
from helpers.useful import Exchange
from DAO.transactionsDao import Queries
from models.transactions import Transactions

class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def test_currency(self):
        datas=6
        result = Exchange.Todayis(datas)
        self.assertEqual(result,4)

    def test_insert_transaction(self)-> list[Transactions]:
        datas=Transactions("",1,0,1,"2023-02-01",80,1,1,"es el testing",1)
        Queries.InsertTransaction(datas)     
        result =Queries.QueryTransaction()
      
        for answer in result:
            if answer.getcomment()=="es el testing":
                answera=answer.getamount()   
        self.assertEqual(answera,80)
        
   
    