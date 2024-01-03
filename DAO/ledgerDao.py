
from models.ledger import Ledger
from models.exchange import Exchange
from config.conf import Inic
from helpers.useful import Exchanges

class Queries:   
    def Losses_byYear(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 300 and accountingtransactions.FkidVAccount < 400 
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 300 and accountingtransactions.FkidVAccount < 400 
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23            
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = []
       
        for answer in answers:
            answer = Ledger( answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9],answer[10],answer[11],answer[12],answer[13])
            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())
            records.append(answer)
        records.append (partialAcum)      
        return records 
        

    def Profits_byYear(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 400 and accountingtransactions.FkidVAccount < 500 
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=1 , amount,0)) + sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 400 and accountingtransactions.FkidVAccount < 500 
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23       
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = []
       
        for answer in answers:
            answer = Ledger( answer[0],answer[1],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9],answer[10],answer[11],answer[12],answer[13])
            
            if answer.getFkidVAccount() > 425 and answer.getFkidVAccount() < 428:          
                exchangeAccounts = Exchanges.importIs(answer.getFkidVAccount())  
 
                for exchangeAccount in exchangeAccounts:
                    exchangeAccount = Exchange(exchangeAccount.getid_Exchange(),exchangeAccount.getdateCoti(),exchangeAccount.getFkidCurrency(),exchangeAccount.getImporteCot()) 
                    monthCotiz = exchangeAccount.getid_Exchange()
                    match monthCotiz:
                        case 1:
                            answer.setjanuary(exchangeAccount.getImporteCot() * answer.getjanuary())
                        case 2:
                            answer.setfebruary(exchangeAccount.getImporteCot() * answer.getfebruary())
                        case 3:
                            answer.setmarch(exchangeAccount.getImporteCot() * answer.getmarch())
                        case 4:
                            answer.setapril(exchangeAccount.getImporteCot() * answer.getapril())
                        case 5:
                            answer.setmay(exchangeAccount.getImporteCot() * answer.getmay())
                        case 6:
                            answer.setjune(exchangeAccount.getImporteCot() * answer.getjune())
                        case 7:
                            answer.setjuly(exchangeAccount.getImporteCot() * answer.getjuly())
                        case 8:
                            answer.setaugust(exchangeAccount.getImporteCot() * answer.getaugust())
                        case 9:
                            answer.setseptember(exchangeAccount.getImporteCot() * answer.getseptember())
                        case 10:
                            answer.setoctober(exchangeAccount.getImporteCot() * answer.getoctober())
                        case 11:
                            answer.setnovember(exchangeAccount.getImporteCot() * answer.getnovember())
                        case 12:
                            answer.setdecember(exchangeAccount.getImporteCot() * answer.getdecember())
            
            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())                
            records.append(answer)



        records.append (partialAcum)      
        return records         

    

    def Assets_byYear(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 0 and accountingtransactions.FkidVAccount < 5
        or accountingtransactions.FkidVAccount > 14 and accountingtransactions.FkidVAccount < 100 
        GROUP BY 
        FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 0 and accountingtransactions.FkidVAccount < 5
        or accountingtransactions.FkidVAccount > 14 and accountingtransactions.FkidVAccount < 100 
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23    
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = [] 
      
        for answer in answers:                                     
           
            answer = Ledger( answer[0],answer[1]
                             ,answer[2]                                                 
                             ,sum(answer[2:4])
                             ,sum(answer[2:5])
                             ,sum(answer[2:6])
                             ,sum(answer[2:7])
                             ,sum(answer[2:8])
                             ,sum(answer[2:9])
                             ,sum(answer[2:10])
                             ,sum(answer[2:11])
                             ,sum(answer[2:12])
                             ,sum(answer[2:13])
                             ,sum(answer[2:14]))
  

            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())
            records.append(answer) 
        records.append(partialAcum)
         
        return records
    
    def Assets_byYear_D(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 15
        GROUP BY 
        FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 15
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23    
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = [] 
      
        for answer in answers:                                     
           
            answer = Ledger( answer[0],answer[1]
                             ,answer[2]                                                 
                             ,sum(answer[2:4])
                             ,sum(answer[2:5])
                             ,sum(answer[2:6])
                             ,sum(answer[2:7])
                             ,sum(answer[2:8])
                             ,sum(answer[2:9])
                             ,sum(answer[2:10])
                             ,sum(answer[2:11])
                             ,sum(answer[2:12])
                             ,sum(answer[2:13])
                             ,sum(answer[2:14]))
  

            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())
            records.append(answer) 
        records.append(partialAcum)
        
       
        return records
    
    def Liabilities_byYear(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 200 and accountingtransactions.FkidVAccount < 300
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2 , amount,0)) - sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=1  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 200 and accountingtransactions.FkidVAccount < 300
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23    
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = []
              
        for answer in answers:
            
                
            answer = Ledger( answer[0],answer[1]
                             ,answer[2]                                                 
                             ,sum(answer[2:4])
                             ,sum(answer[2:5])
                             ,sum(answer[2:6])
                             ,sum(answer[2:7])
                             ,sum(answer[2:8])
                             ,sum(answer[2:9])
                             ,sum(answer[2:10])
                             ,sum(answer[2:11])
                             ,sum(answer[2:12])
                             ,sum(answer[2:13])
                             ,sum(answer[2:14]))

            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())
            records.append(answer)
        records.append (partialAcum)      
    
        return records
    
    def Assets_byYearD(year) -> list[Ledger]:  
        query23 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-01-01' and '2023-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-02-01' and '2023-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-03-01' and '2023-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-04-01' and '2023-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-05-01' and '2023-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-06-01' and '2023-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-07-01' and '2023-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-08-01' and '2023-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-09-01' and '2023-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-10-01' and '2023-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-11-01' and '2023-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2023-12-01' and '2023-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 12
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 

        query24 ="""SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
        , sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-01-01' and '2024-01-31' and FkidVIncreasedBY=2  , amount,0)) as enero
        , sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-02-01' and '2024-02-28' and FkidVIncreasedBY=2  , amount,0)) as febrero
        , sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-03-01' and '2024-03-31' and FkidVIncreasedBY=2  , amount,0)) as marzo
        , sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-04-01' and '2024-04-30' and FkidVIncreasedBY=2  , amount,0)) as abril
        , sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-05-01' and '2024-05-31' and FkidVIncreasedBY=2  , amount,0)) as mayo
        , sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-06-01' and '2024-06-30' and FkidVIncreasedBY=2  , amount,0)) as junio
        , sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-07-01' and '2024-07-31' and FkidVIncreasedBY=2  , amount,0)) as julio
        , sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-08-01' and '2024-08-31' and FkidVIncreasedBY=2  , amount,0)) as agosto
        , sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-09-01' and '2024-09-30' and FkidVIncreasedBY=2  , amount,0)) as septiembre
        , sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-10-01' and '2024-10-31' and FkidVIncreasedBY=2  , amount,0)) as octubre
        , sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-11-01' and '2024-11-30' and FkidVIncreasedBY=2  , amount,0)) as noviembre
        , sum(if(accruedDate between'2024-12-01' and '2042-12-31' and FkidVIncreasedBY=1 , amount,0)) - sum(if(accruedDate between'2024-12-01' and '2024-12-31' and FkidVIncreasedBY=2  , amount,0)) as diciembre
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 12
        GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]
        query=" "
        if year == 2024:
            query = query24
        else:
            query = query23
        answers = Inic.db_connect(query,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = [] 
      
        for answer in answers:                                     
           
            answer = Ledger( answer[0],answer[1]
                             ,answer[2]                                                 
                             ,sum(answer[2:4])
                             ,sum(answer[2:5])
                             ,sum(answer[2:6])
                             ,sum(answer[2:7])
                             ,sum(answer[2:8])
                             ,sum(answer[2:9])
                             ,sum(answer[2:10])
                             ,sum(answer[2:11])
                             ,sum(answer[2:12])
                             ,sum(answer[2:13])
                             ,sum(answer[2:14]))
                     
            partialAcum = Ledger("","Total",partialAcum.getjanuary() + answer.getjanuary(),partialAcum.getfebruary() + answer.getfebruary()
                                  ,partialAcum.getmarch() + answer.getmarch(),partialAcum.getapril() + answer.getapril()
                                  ,partialAcum.getmay() + answer.getmay(),partialAcum.getjune() + answer.getjune()
                                  ,partialAcum.getjuly() + answer.getjuly(),partialAcum.getaugust() + answer.getaugust()
                                  ,partialAcum.getseptember() + answer.getseptember(),partialAcum.getoctober() + answer.getoctober()
                                  ,partialAcum.getnovember() + answer.getnovember(),partialAcum.getdecember() + answer.getdecember())
            records.append(answer) 
        records.append(partialAcum)
       
        return records   