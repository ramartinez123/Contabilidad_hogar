from app import mysql
from models.transactions import Transactions
from config.conf import Inic
from helpers.useful import Exchanges

class Queries:   
    def QueryTransaction() -> list[Transactions]:  
        query ="""SELECT accountingtransactions.*,accounts.account FROM accountingtransactions 
        INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount
        ORDER BY accountingtransactions.idAccountingTransaction ASC"""
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records=[]
        for answer in answers:
                 answer = Transactions( answer[0],answer[10],answer[2],answer[3],answer[4]
                                       ,answer[5],answer[6],answer[7],answer[8],answer[9])
                 records.append(answer)
        return records 
            
    def InsertTransaction(transaction:Transactions) -> Transactions:
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY,accruedDate
        ,amount,FKidCountry,FkidCity,comment,FkidDues)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        Queries.UpdateExchange()
        parameters=[transaction.getFkidVAccount(),transaction.getFkidSubAccount(),
                    transaction.getFkidVIncreasedBY(),transaction.getaccruedDate(),transaction.getamount(),
                    transaction.getFKidCountry(),
                    transaction.getFkidCity(),transaction.getcomment(),transaction.getFkidDues()]
                 
        Inic.db_insert(query,parameters)    

    def QuerybyDate(transaction:Transactions) -> list[Transactions]: 
        query ="""SELECT accountingtransactions.*,accounts.account FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount
        where aaccountingtransactions.accruedDate == (%s) """ 
        parameters=[transaction.getaccruedDate()]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = Transactions( answer[0],answer[10],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9])
            records.append(answer)
        return records 
    
    def InsertExchange() -> list[Transactions]:
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY,accruedDate
        ,amount,FKidCountry,FkidCity,comment,FkidDues)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        transactions=Exchanges.UpdateExchange()
        for transaction in transactions:
          parameters=[transaction.getFkidVAccount(),transaction.getFkidSubAccount(),
                    transaction.getFkidVIncreasedBY(),transaction.getaccruedDate(),transaction.getamount(),
                    transaction.getFKidCountry(),
                    transaction.getFkidCity(),transaction.getcomment(),transaction.getFkidDues()  ]       
          Inic.db_insert(query,parameters) 

    
   
                   
    