
from models.transactions import Transactions
from config.conf import Inic

class Queries:   
    def InsertQuickTransac(transaction:Transactions) -> Transactions:
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY
        ,accruedDate,amount,FKidCountry,FkidCity,comment,FkidDues) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        account = transaction.getFkidVAccount()
        match account:
            case "1":
                transaction.setFkidVAccount(341)
            case "2":
                transaction.setFkidVAccount(331)    
            case "3":
                transaction.setFkidVAccount(333)
            case "4":
                transaction.setFkidVAccount(17)
            case "5":
                transaction.setFkidVAccount(342)
            case "6":
                transaction.setFkidVAccount(304)
            case "7":
                transaction.setFkidVAccount(305)
            case "8":
                transaction.setFkidVAccount(301)
            case "9":
                transaction.setFkidVAccount(306)
            case "10":
                transaction.setFkidVAccount(307)
            case "11":
                transaction.setFkidVAccount(311)
            case "31":
                transaction.setFkidVAccount(1)
            case "32":
                transaction.setFkidVAccount(210)
            case "33":
                transaction.setFkidVAccount(212)
            case "34":
                transaction.setFkidVAccount(211)
            case "35":
                transaction.setFkidVAccount(213)
            case "36":
                transaction.setFkidVAccount(13)

        parameters=[transaction.getFkidVAccount(),transaction.getFkidSubAccount(),
                    transaction.getFkidVIncreasedBY(),transaction.getaccruedDate(),transaction.getamount(),
                    transaction.getFKidCountry(),
                    transaction.getFkidCity(),transaction.getcomment(),transaction.getFkidDues()]
        
        Inic.db_insert(query,parameters)    

        