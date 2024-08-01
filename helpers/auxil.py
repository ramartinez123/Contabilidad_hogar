from models.exchange import Exchange
from models.ledger import Ledger
from config.conf import Inic
from models.transactions import Transactions
from typing import List


class Exchangesa:    
        
    def Todayis(curr):

        currx = int(curr)
            
        if currx > 4 and currx < 9 :
            curry = 4 
               
        elif currx == 9:
            curry = 6  
                
        elif currx == 10:
            curry = 7   
                
        elif currx == 11:
            curry = 8 

        elif currx == 33:
            curry = 4

        elif currx == 51:
            curry = 4

        elif currx == 426:
            curry = 4

        elif currx == 427:
            curry = 4

        elif currx == 15:
            curry = 4

        elif currx == 421:
            curry = 4
        
        else:
            curry = 1
        return(curry)
    
   

    def importIs(importa) -> list[Exchange]: 
        curra = Exchangesa.Todayis(importa)
        parameters=[curra]
        query23 ="""SELECT MONTH (dateCoti) as mes, dateCoti, FKidCurrency, ImporteCot from exchange 
                    WHERE dateCoti in (SELECT MAX(dateCoti) and dateCoti > '2024-01-01'from exchange
                                       GROUP BY MONTH (dateCoti), FKidCurrency) and FKidCurrency = (%s)"""
        query24 ="""SELECT MONTH (dateCoti) as mes, dateCoti, FKidCurrency, ImporteCot from exchange 
                    WHERE dateCoti > '2023-12-31' and dateCoti in (SELECT MAX(dateCoti) from exchange
                                       GROUP BY MONTH (dateCoti), FKidCurrency) and FKidCurrency = (%s)"""

        records =[]
        answers = Inic.db_connect(query24,parameters)
        """for answer in answers:
            answer = Exchange(answer[0],answer[1],answer[2],answer[3]) 
            records.append(answer)"""
        
        records = [Exchange(*answer) for answer in answers]
        
        return records
    
    