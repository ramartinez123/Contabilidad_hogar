
from models.account import Account
from config.conf import Inic

class QueriesAccount:   
    def QueryAccount() -> list[Account]:  
        query ="""SELECT idAccount,account,accounttypes.accountType,accountingitems.accountingItem,FkidIncreasedBY,FkidAccountingMethod,FKidCurrency,Detalle  
        FROM accounts 
        INNER JOIN accounttypes ON accounts.FkidAccountType = accounttypes.idAccountType 
        INNER JOIN accountingItems ON accounts.FkidAccountingItem = accountingitems.idAccountingItem """
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = Account( answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7])
            records.append(answer)
        return records 
    
            
    def Insert(account:Account) -> Account:
        query ="INSERT INTO accounts (account,FkidVAccountType,FkidAccountingItem,FkidVIncreasedBY,FkidAccountingMethod,FKidCourrency,Detalle) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        parameters=[account.getFAccount(),account.getFkidVAccountType(),
                    account.getFkidAccountingItem(),account.getFkidVIncreasedBY(),account.FkidAccountingMethod(),
                    account.getFKidCourrency(),
                    account.Detalle()]
                 
        Inic.db_insert(query,parameters)    

    def QueryAccountNames():
        query ="""SELECT idAccount,account
        FROM accounts """
        parameters=[]
        answer = Inic.db_connect(query,parameters)
        return answer
    
    def QueryAccountCountries():  
        query ="""SELECT idCountry,country
        FROM countries """
        parameters=[]
        answerCountry = Inic.db_connect(query,parameters)
        return answerCountry

    def QueryAccountCities():  
        query ="""SELECT idCity,city
        FROM cities """
        parameters=[]
        answerCity = Inic.db_connect(query,parameters)
        return answerCity
    
 