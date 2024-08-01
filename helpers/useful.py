from models.exchange import Exchange
from models.ledger import Ledger
from config.conf import Inic
from models.transactions import Transactions
from helpers.auxil import Exchangesa


class Exchanges:    
           
    def UpdateExchange() -> list[Transactions]:
        """query23 =SELECT accountingtransactions.FkidVAccount as Codigo, accounts.account as Cuenta
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
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 16
        or accountingtransactions.FkidVAccount = 421 GROUP BY FkidVAccount ORDER BY FkidVAccount  """

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
        FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount WHERE accountingtransactions.FkidVAccount > 4 and accountingtransactions.FkidVAccount < 16
        or accountingtransactions.FkidVAccount = 421 GROUP BY FkidVAccount ORDER BY FkidVAccount """
        
        parameters=[]  
        a5_1=a5_2=a5_3=a5_4=a5_5=a5_6=a5_7=a5_8=a5_9=a5_10=a5_11=a5_12=0
        a6_1=a6_2=a6_3=a6_4=a6_5=a6_6=a6_7=a6_8=a6_9=a6_10=a6_11=a6_12=0
        a7_1=a7_2=a7_3=a7_4=a7_5=a7_6=a7_7=a7_8=a7_9=a7_10=a7_11=a7_12=0
        a8_1=a8_2=a8_3=a8_4=a8_5=a8_6=a8_7=a8_8=a8_9=a8_10=a8_11=a8_12=0
        a9_1=a9_2=a9_3=a9_4=a9_5=a9_6=a9_7=a9_8=a9_9=a9_10=a9_11=a9_12=0 
        a10_1=a10_2=a10_3=a10_4=a10_5=a10_6=a10_7=a10_8=a10_9=a10_10=a10_11=a10_12=0
        a11_1=a11_2=a11_3=a11_4=a11_5=a11_6=a11_7=a11_8=a11_9=a11_10=a11_11=a11_12=0
        a16_1=a16_2=a16_3=a16_4=a16_5=a16_6=a16_7=a16_8=a16_9=a16_10=a16_11=a16_12=0
        dif15_1=dif15_2=dif15_3=dif15_4=dif15_5=dif15_6=dif15_7=dif15_8=dif15_9=dif15_10=dif15_11=dif15_12=0
        answers = Inic.db_connect(query24,parameters)     
       
        # Recorre cuentas en moneda extranjera
        for answer in answers:                                         
            answer = Ledger( answer[0],answer[1],
                             answer[2] ,sum(answer[2:4]) ,sum(answer[2:5]),                                                                                       
                             sum(answer[2:6]),sum(answer[2:7]),sum(answer[2:8]),
                             sum(answer[2:9]),sum(answer[2:10]),sum(answer[2:11]),
                             sum(answer[2:12]),sum(answer[2:13]),sum(answer[2:14]))  
                              
            #Recorre datos cotizaciones monedas extranjeras
            exchangeAccounts = Exchangesa.importIs(answer.getFkidVAccount())  
            for exchangeAccount in exchangeAccounts:
                    exchangeAccount = Exchange(
                       exchangeAccount.getid_Exchange(),
                       exchangeAccount.getdateCoti(),
                       exchangeAccount.getFkidCurrency(),
                       exchangeAccount.getImporteCot()) 
                    
                    monthCotiz = exchangeAccount.getid_Exchange()
                    accountCotiz = answer.getFkidVAccount()    

                    #Evalua el mes y la cuenta
                    match monthCotiz:
                        case 1:     
                            result_1= exchangeAccount.getImporteCot() * answer.getjanuary()                     
                            match accountCotiz:
                                case 5:a5_1=result_1
                                case 6:a6_1=result_1
                                case 7:a7_1=result_1
                                case 8:a8_1=result_1
                                case 9:a9_1=result_1
                                case 10:a10_1=result_1
                                case 11:a11_1=result_1
                                case 421:a16_1=answer.getjanuary()

                        case 2:
                            result_1= exchangeAccount.getImporteCot() * answer.getfebruary()
                            match accountCotiz:
                                case 5:a5_2=result_1                                
                                case 6:a6_2=result_1                                
                                case 7:a7_2=result_1                              
                                case 8:a8_2=result_1                              
                                case 9:a9_2=result_1                             
                                case 10:a10_2=result_1                           
                                case 11:a11_2=result_1                              
                                case 421:a16_2=answer.getfebruary()
                                  
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
                            result_1= exchangeAccount.getImporteCot() * answer.getjuly()
                            match accountCotiz:
                                case 5:
                                  a5_7=result_1
                                case 6:
                                  a6_7=result_1
                                case 7:
                                  a7_7=result_1
                                case 8:
                                  a8_7=result_1
                                case 9:
                                  a9_7=result_1
                                case 10:
                                  a10_7=result_1
                                case 11:
                                  a11_7=result_1
                                case 421:
                                  a16_7=answer.getjuly()
                        case 8:
                            result_1= exchangeAccount.getImporteCot() * answer.getaugust()
                            match accountCotiz:
                                case 5:
                                  a5_8=result_1
                                case 6:
                                  a6_8=result_1
                                case 7:
                                  a7_8=result_1
                                case 8:
                                  a8_8=result_1
                                case 9:
                                  a9_8=result_1
                                case 10:
                                  a10_8=result_1
                                case 11:
                                  a11_8=result_1
                                case 421:
                                  a16_8=answer.getaugust()                            
                        case 9:
                            result_1= exchangeAccount.getImporteCot() * answer.getseptember()
                            match accountCotiz:
                                case 5:
                                  a5_9=result_1
                                case 6:
                                  a6_9=result_1
                                case 7:
                                  a7_9=result_1
                                case 8:
                                  a8_9=result_1
                                case 9:
                                  a9_9=result_1
                                case 10:
                                  a10_9=result_1
                                case 11:
                                  a11_9=result_1
                                case 421:
                                  a16_9=answer.getseptember()                      
                        case 10:
                            result_1= exchangeAccount.getImporteCot() * answer.getoctober()
                            match accountCotiz:
                                case 5:
                                  a5_10=result_1
                                case 6:
                                  a6_10=result_1
                                case 7:
                                  a7_10=result_1
                                case 8:
                                  a8_10=result_1
                                case 9:
                                  a9_10=result_1
                                case 10:
                                  a10_10=result_1
                                case 11:
                                  a11_10=result_1
                                case 421:
                                  a16_10=answer.getoctober()                            
                        case 11:
                            result_1= exchangeAccount.getImporteCot() * answer.getnovember()
                            match accountCotiz:
                                case 5:
                                  a5_11=result_1
                                case 6:
                                  a6_11=result_1
                                case 7:
                                  a7_11=result_1
                                case 8:
                                  a8_11=result_1
                                case 9:
                                  a9_11=result_1
                                case 10:
                                  a10_11=result_1
                                case 11:
                                  a11_11=result_1
                                case 421:
                                  a16_11=answer.getnovember()
                        case 12:
                            result_1= exchangeAccount.getImporteCot() * answer.getdecember()
                            match accountCotiz:
                                case 5:
                                  a5_12=result_1
                                case 6:
                                  a6_12=result_1
                                case 7:
                                  a7_12=result_1
                                case 8:
                                  a8_12=result_1
                                case 9:
                                  a9_12=result_1
                                case 10:
                                  a10_12=result_1
                                case 11:
                                  a11_12=result_1
                                case 421:
                                  a16_6=answer.getdecember()
      
        dif15_1 =a5_1 + a6_1 + a7_1 + a8_1 + a9_1 + a10_1 + a11_1
        dif15_2 =a5_2-a5_1 + a6_2-a6_1 + a7_2-a7_1 + a8_2-a8_1 + a9_2-a9_1 + a10_2-a10_1 + a11_2-a11_1
        dif15_3 =a5_3-a5_2 + a6_3-a6_2 + a7_3-a7_2 + a8_3-a8_2 + a9_3-a9_2 + a10_3-a10_2 + a11_3-a11_2
        dif15_4 =a5_4-a5_3 + a6_4-a6_3 + a7_4-a7_3 + a8_4-a8_3 + a9_4-a9_3 + a10_4-a10_3 + a11_4-a11_3
        dif15_5 =a5_5-a5_4 + a6_5-a6_4 + a7_5-a7_4 + a8_5-a8_4 + a9_5-a9_4 + a10_5-a10_4 + a11_5-a11_4
        dif15_6 =a5_6-a5_5 + a6_6-a6_5 + a7_6-a7_5 + a8_6-a8_5 + a9_6-a9_5 + a10_6-a10_5 + a11_6-a11_5
        dif15_7 =a5_7-a5_6 + a6_7-a6_6 + a7_7-a7_6 + a8_7-a8_6 + a9_7-a9_6 + a10_7-a10_6 + a11_7-a11_6
        dif15_8 =a5_8-a5_7 + a6_8-a6_7 + a7_8-a7_7 + a8_8-a8_7 + a9_8-a9_7 + a10_8-a10_7 + a11_8-a11_7
        dif15_9 =a5_9-a5_8 + a6_9-a6_8 + a7_9-a7_8 + a8_9-a8_8 + a9_9-a9_8 + a10_9-a10_8 + a11_9-a11_8
        dif15_10 =a5_10-a5_9 + a6_10-a6_9 + a7_10-a7_9 + a8_10-a8_9 + a9_10-a9_9 + a10_10-a10_9 + a11_10-a11_9
        dif15_11 =a5_11-a5_10 + a6_11-a6_10 + a7_11-a7_10 + a8_11-a8_10 + a9_11-a9_10 + a10_11-a10_10 + a11_11-a11_10
        dif15_12 =a5_12-a5_11 + a6_12-a6_11 + a7_12-a7_11 + a8_12-a8_11 + a9_12-a9_11 + a10_12-a10_11 + a11_12-a11_11

        reply =[]
        
        def process_dif(dif, a16, date):
           legend = "Asiento automatico"
           if a16 != 0 and dif != 0:
              dif -= (a16 * -1)
           if dif != 0:
              dif_o = Transactions("", 15, 0, 1, date, dif, 1, 1, legend, 0)
              dif421_o = Transactions("", 421, 0, 2, date, dif, 1, 1, legend, 0)
              reply.append(dif_o)
              reply.append(dif421_o)

        process_dif(dif15_1, a16_1, '2024-01-28')
        process_dif(dif15_2, a16_1, '2024-02-28')
        process_dif(dif15_3, a16_2, '2024-03-28')
        process_dif(dif15_4, a16_3, '2024-04-28')
        process_dif(dif15_5, a16_4, '2024-05-28')
        process_dif(dif15_6, a16_5, '2024-06-28')
        process_dif(dif15_7, a16_6, '2024-07-28')
        process_dif(dif15_8, a16_7, '2024-08-28')
        process_dif(dif15_9, a16_8, '2024-09-28')
        process_dif(dif15_10, a16_9, '2024-10-28')
        process_dif(dif15_11, a16_10, '2024-11-28')
        process_dif(dif15_12, a16_11, '2024-12-28')

        return reply
