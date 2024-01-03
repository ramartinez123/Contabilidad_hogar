from models.exchange import Exchange
from models.ledger import Ledger
from config.conf import Inic
from models.transactions import Transactions

class Exchanges:    
        
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
        curra = Exchanges.Todayis(importa)
        parameters=[curra]
        query ="""SELECT MONTH (dateCoti) as mes, dateCoti, FKidCurrency, ImporteCot from exchange 
                    WHERE dateCoti in (SELECT MAX(dateCoti) from exchange
                                       GROUP BY MONTH (dateCoti), FKidCurrency) and FKidCurrency = (%s)"""
        records =[]
        answers = Inic.db_connect(query,parameters)
        for answer in answers:
            answer = Exchange(answer[0],answer[1],answer[2],answer[3])   
            records.append(answer)
        return records
    
    def UpdateExchange() -> list[Transactions]:
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
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 52
        or accountingtransactions.FkidVAccount = 421 GROUP BY FkidVAccount ORDER BY FkidVAccount """  

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
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 52
        or accountingtransactions.FkidVAccount = 421 GROUP BY FkidVAccount ORDER BY FkidVAccount """ 
        parameters=[]  
        answers = Inic.db_connect(query23,parameters)
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = [] 
        
        a5_1=a5_2=a6_1=a6_2=a7_1=a7_2=a8_1=a8_2=a9_2=a9_1=a10_1=a10_2=a11_1=a11_2=dif15_2=a15_1=a15_2=a16_1=a16_2=0
        a5_3=a5_4=a6_3=a6_4=a7_3=a7_4=a8_3=a8_4=a9_3=a9_4=a10_3=a10_4=a11_3=a11_4=dif15_4=a15_3=a15_4=a16_3=a16_4=0
        a5_5=a5_6=a6_5=a6_6=a7_5=a7_6=a8_5=a8_6=a9_5=a9_6=a10_5=a10_6=a11_5=a11_6=dif15_6=a15_5=a15_6=a16_5=a16_6=0              
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


            exchangeAccounts = Exchanges.importIs(answer.getFkidVAccount())  
            for exchangeAccount in exchangeAccounts:
                    exchangeAccount = Exchange(exchangeAccount.getid_Exchange(),exchangeAccount.getdateCoti(),exchangeAccount.getFkidCurrency(),exchangeAccount.getImporteCot()) 
                    monthCotiz = exchangeAccount.getid_Exchange()
                    accountCotiz = answer.getFkidVAccount()
                    match monthCotiz:
                        case 1:
                            result_1= exchangeAccount.getImporteCot() * answer.getjanuary()
                            match accountCotiz:
                                case 5:
                                  a5_1=result_1
                                case 6:
                                  a6_1=result_1
                                case 7:
                                  a7_1=result_1
                                case 8:
                                  a8_1=result_1
                                case 9:
                                  a9_1=result_1
                                case 10:
                                  a10_1=result_1
                                case 11:
                                  a11_1=result_1
                                case 421:
                                  a16_1=answer.getjanuary()

                        case 2:
                            result_1= exchangeAccount.getImporteCot() * answer.getfebruary()
                            match accountCotiz:
                                case 5:
                                  a5_2=result_1
                                case 6:
                                  a6_2=result_1
                                case 7:
                                  a7_2=result_1
                                case 8:
                                  a8_2=result_1
                                case 9:
                                  a9_2=result_1
                                case 10:
                                  a10_2=result_1
                                case 11:
                                  a11_2=result_1
                                case 421:
                                  a16_2=answer.getfebruary()
                        case 3:
                            result_1= exchangeAccount.getImporteCot() * answer.getmarch()
                            match accountCotiz:
                                case 5:
                                  a5_3=result_1
                                case 6:
                                  a6_3=result_1
                                case 7:
                                  a7_3=result_1
                                case 8:
                                  a8_3=result_1
                                case 9:
                                  a9_3=result_1
                                case 10:
                                  a10_3=result_1
                                case 11:
                                  a11_3=result_1
                                case 421:
                                  a16_3=answer.getmarch()
                        case 4:
                            result_1= exchangeAccount.getImporteCot() * answer.getapril()
                            match accountCotiz:
                                case 5:
                                  a5_4=result_1
                                case 6:
                                  a6_4=result_1
                                case 7:
                                  a7_4=result_1
                                case 8:
                                  a8_4=result_1
                                case 9:
                                  a9_4=result_1
                                case 10:
                                  a10_4=result_1
                                case 11:
                                  a11_4=result_1
                                case 421:
                                  a16_4=answer.getapril()

                        case 5:
                            result_1= exchangeAccount.getImporteCot() * answer.getmay()
                            match accountCotiz:
                                case 5:
                                  a5_5=result_1
                                case 6:
                                  a6_5=result_1
                                case 7:
                                  a7_5=result_1
                                case 8:
                                  a8_5=result_1
                                case 9:
                                  a9_5=result_1
                                case 10:
                                  a10_5=result_1
                                case 11:
                                  a11_5=result_1
                                case 421:
                                  a16_5=answer.getmay()

                        case 6:
                            result_1= exchangeAccount.getImporteCot() * answer.getjune()
                            match accountCotiz:
                                case 5:
                                  a5_6=result_1
                                case 6:
                                  a6_6=result_1
                                case 7:
                                  a7_6=result_1
                                case 8:
                                  a8_6=result_1
                                case 9:
                                  a9_6=result_1
                                case 10:
                                  a10_6=result_1
                                case 11:
                                  a11_6=result_1
                                case 421:
                                  a16_6=answer.getjune()
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

        reply =[]
        dif15_1 =a5_1 + a6_1 + a7_1 + a8_1 + a9_1 + a10_1 + a11_1-410000  
        if a16_1 !=0:
            dif15_1=dif15_1 -((a16_1*-1))
        if dif15_1 != 0:
            dif15_1o=Transactions("",15,0,1,'2023-01-28',dif15_1,1,1,"Asiento automatico",0)
            dif421_1o=Transactions("",421,0,2,'2023-01-28',dif15_1,1,1,"Asiento automatico",0)
            reply.append(dif15_1o)
            reply.append(dif421_1o)

        dif15_2 =a5_2-a5_1 + a6_2-a6_1 + a7_2-a7_1 + a8_2-a8_1 + a9_2-a9_1 + a10_2-a10_1 + a11_2-a11_1
        if a16_2 !=0:
            dif15_2=dif15_2 -((a16_2*-1)-(a16_1*-1))
        if dif15_2 != 0:
            dif15_2o=Transactions("",15,0,1,'2023-02-28',dif15_2,1,1,"Asiento automatico",0)
            dif421_2o=Transactions("",421,0,2,'2023-02-28',dif15_2,1,1,"Asiento automatico",0)
            reply.append(dif15_2o)
            reply.append(dif421_2o)

        dif15_3 =a5_3-a5_2 + a6_3-a6_2 + a7_3-a7_2 + a8_3-a8_2 + a9_3-a9_2 + a10_3-a10_2 + a11_3-a11_2
        if a16_3 !=0:
            dif15_3=dif15_3 -((a16_3*-1)-(a16_2*-1))
        if dif15_3 != 0:
            dif15_3o=Transactions("",15,0,1,'2023-03-28',dif15_3,1,1,"Asiento automatico",0)
            dif421_3o=Transactions("",421,0,2,'2023-03-28',dif15_3,1,1,"Asiento automatico",0)
            reply.append(dif15_3o)
            reply.append(dif421_3o)

        dif15_4 =a5_4-a5_3 + a6_4-a6_3 + a7_4-a7_3 + a8_4-a8_3 + a9_4-a9_3 + a10_4-a10_3 + a11_4-a11_3
        if a16_4 !=0:
            dif15_4=dif15_4 -((a16_4*-1)-(a16_3*-1))
        if dif15_4 != 0:
            dif15_4o=Transactions("",15,0,1,'2023-04-28',dif15_4,1,1,"Asiento automatico",0)
            dif421_4o=Transactions("",421,0,2,'2023-04-28',dif15_4,1,1,"Asiento automatico",0)
            reply.append(dif15_4o)
            reply.append(dif421_4o)

        dif15_5 =a5_5-a5_4 + a6_5-a6_4 + a7_5-a7_4 + a8_5-a8_4 + a9_5-a9_4 + a10_5-a10_4 + a11_5-a11_4
        if a16_5 !=0:
            dif15_5=dif15_5 -((a16_5*-1)-(a16_4*-1))
        if dif15_5 != 0:
            dif15_5o=Transactions("",15,0,1,'2023-05-28',dif15_5,1,1,"Asiento automatico",0)
            dif421_5o=Transactions("",421,0,2,'2023-05-28',dif15_5,1,1,"Asiento automatico",0)
            reply.append(dif15_5o)
            reply.append(dif421_5o)

        dif15_6 =a5_6-a5_5 + a6_6-a6_5 + a7_6-a7_5 + a8_6-a8_5 + a9_6-a9_5 + a10_6-a10_5 + a11_6-a11_5
        if a16_6 !=0:
            dif15_6=dif15_6 -((a16_6*-1)-(a16_5*-1))
        if dif15_6 != 0:
            dif15_6o=Transactions("",15,0,1,'2023-06-28',dif15_6,1,1,"Asiento automatico",0)
            dif421_6o=Transactions("",421,0,2,'2023-06-28',dif15_6,1,1,"Asiento automatico",0)
            reply.append(dif15_6o)
            reply.append(dif421_6o)

        return reply
               
    