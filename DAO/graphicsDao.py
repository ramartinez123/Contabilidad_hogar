from config.conf import Inic
from models.exchange import Exchange

class Queries:   
    def LossesGraphic():  
        query ="""SELECT 
        MONTH (accruedDate) as mes,  sum(if(FkidVIncreasedBY=1 , amount,0)) - sum(if(FkidVIncreasedBY=2  , amount,0)) as MES 
            FROM accountingtransactions  
            WHERE accountingtransactions.FkidVAccount > 300 and accountingtransactions.FkidVAccount < 400 
            AND accruedDate > '2024-12-31' AND accruedDate < '2026-01-01'
            GROUP BY MONTH (accruedDate)  """ 
        parameters=[]
        answer= Inic.db_connect(query,parameters)
        return answer 

    def Losses_byGraphic():  
        query ="""SELECT  accounts.account, SUM(accountingtransactions.amount) as tot
                    FROM accountingtransactions  inner JOIN accounts  
                    on accountingtransactions.FkidVAccount = accounts.idAccount 
                    WHERE FkidVAccount >300 and FkidVAccount  <400 and accruedDate> '2024-12-31' AND accruedDate < '2026-01-01' GROUP BY FkidVAccount  """ 
        parameters=[]
        answer= Inic.db_connect(query,parameters)
        return answer 
        
    def AssetsGraphics():  
        query ="""SELECT 
        MONTH (accruedDate) as mes,  sum(if(FkidVIncreasedBY=1 , amount,0)) - sum(if(FkidVIncreasedBY=2  , amount,0)) as MES 
            FROM accountingtransactions  
            WHERE (accountingtransactions.FkidVAccount > 0 and accountingtransactions.FkidVAccount < 5 or accountingtransactions.FkidVAccount > 14  and accountingtransactions.FkidVAccount <100)
            AND accruedDate > '2024-12-31' AND accruedDate < '2026-01-01'
            GROUP BY MONTH (accruedDate)  """ 
        parameters=[]
        answers= Inic.db_connect(query,parameters)

        records = [] 
        acu=0
        for answer in answers:                                     
            acu += answer[1]

            records.append((answer[0],acu))
        return records 
    
    def LiabilitiesGraphics():  
        query ="""SELECT 
        MONTH (accruedDate) as mes,  sum(if(FkidVIncreasedBY=2 , amount,0)) - sum(if(FkidVIncreasedBY=1  , amount,0)) as MES 
            FROM accountingtransactions  
            WHERE accountingtransactions.FkidVAccount > 200 and accountingtransactions.FkidVAccount < 300 
            AND accruedDate > '2024-12-31' AND accruedDate < '2026-01-01'
            GROUP BY MONTH (accruedDate)  """ 
        parameters=[]
        answers= Inic.db_connect(query,parameters)

        records = [] 
        acu=0
        for answer in answers:                                     
            acu += answer[1]
            records.append((answer[0],acu))
        return records

    def dolar_cotiz()-> list[Exchange]:
        query= """SELECT * FROM `exchange`
            WHERE `FKidCurrency`=4 AND DATE(`dateCoti`) >= DATE_SUB(LAST_DAY(CURDATE()), INTERVAL 1 MONTH)
            AND DATE(`dateCoti`) <= LAST_DAY(CURDATE())"""
        parameters=[]
        answers= Inic.db_connect(query,parameters)
        return answers