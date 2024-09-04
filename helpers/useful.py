from models.exchange import Exchange
from models.ledger import Ledger
from config.conf import Inic
from models.transactions import Transactions
from helpers.auxil import Exchangesa
from datetime import datetime

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

        # Diccionarios para almacenar los valores
        a_dict = {account: {month: 0 for month in range(1, 13)} for account in [5, 6, 7, 8, 9, 10, 11]}
        a16_dict = {month: 0 for month in range(1, 13)}
        dif15_dict = {month: 0 for month in range(1, 13)}
 
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
                            result_1 = exchangeAccount.getImporteCot() * answer.getjanuary()
                            if accountCotiz in a_dict:
                            # Actualiza el valor en a_dict para la cuenta y el mes de febrero (2)
                                a_dict[accountCotiz][1] = result_1
                            elif accountCotiz == 421:
                            # Actualiza el valor en a16_dict para el mes de febrero (2)
                                a16_dict[1] = answer.getjanuary()
                                

                        case 2:
                            result_1 = exchangeAccount.getImporteCot() * answer.getfebruary()
                            if accountCotiz in a_dict:
                            # Actualiza el valor en a_dict para la cuenta y el mes de febrero (2)
                                a_dict[accountCotiz][2] = result_1
                            elif accountCotiz == 421:
                            # Actualiza el valor en a16_dict para el mes de febrero (2)
                                a16_dict[2] = answer.getfebruary()
                               
                        case 3:
                            result_1= exchangeAccount.getImporteCot() * answer.getmarch()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][3] = result_1
                            elif accountCotiz == 421:
                                a16_dict[3]=answer.getmarch()

                        case 4:
                            result_1= exchangeAccount.getImporteCot() * answer.getapril()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][4] = result_1
                            elif accountCotiz == 421:
                                a16_dict[4]=answer.getapril()
                        case 5:
                            result_1= exchangeAccount.getImporteCot() * answer.getmay()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][5] = result_1
                            elif accountCotiz == 421:
                                a16_dict[5]=answer.getmay()
                        case 6:
                            result_1= exchangeAccount.getImporteCot() * answer.getjune()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][6] = result_1
                            elif accountCotiz == 421:
                                a16_dict[6]=answer.getjune()
                        case 7:
                            result_1= exchangeAccount.getImporteCot() * answer.getjuly()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][7] = result_1
                            elif accountCotiz == 421:
                                a16_dict[7]=answer.getjuly()
                        case 8:
                            result_1= exchangeAccount.getImporteCot() * answer.getaugust()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][8] = result_1
                            elif accountCotiz == 421:
                                a16_dict[8]=answer.getaugust()                        
                        case 9:
                            result_1= exchangeAccount.getImporteCot() * answer.getseptember()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][9] = result_1
                            elif accountCotiz == 421:
                                a16_dict[9]=answer.getseptember()                     
                        case 10:
                            result_1= exchangeAccount.getImporteCot() * answer.getoctober()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][10] = result_1
                            elif accountCotiz == 421:
                                a16_dict[10]=answer.getoctober()                          
                        case 11:
                            result_1= exchangeAccount.getImporteCot() * answer.getnovember()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][11] = result_1
                            elif accountCotiz == 421:
                                a16_dict[11]=answer.getnovember()
                        case 12:
                            result_1= exchangeAccount.getImporteCot() * answer.getdecember()
                            if accountCotiz in a_dict:
                                a_dict[accountCotiz][12] = result_1
                            elif accountCotiz == 421:
                                a16_dict[12]=answer.getdecember()

        # Inicializa las diferencias
        differences = {month: 0 for month in range(1, 13)}

        differences[1] = sum(a_dict[account][1] for account in [5, 6, 7, 8, 9, 10, 11])

        for month in range(2, 13): 
            differences[month] = sum(a_dict[account][month] - a_dict[account][month-1] for account in [5, 6, 7, 8, 9, 10, 11])
            print(differences[month])
        print(a_dict)
        print(a16_dict)

        
        reply =[]

        #Registra asientos productos de diferencias de cotizacion    
        current_year = datetime.now().year    
        
        def process_dif(dif, a16, date):         
            legend = "Asiento automatico"
            if a16 != 0 and dif != 0:
                dif -= (a16 * -1)    
                print ( "el primero" )

            elif dif != 0:
                dif_o = Transactions("", 15, 0, 1, date, dif, 1, 1, legend, 0)
                dif421_o = Transactions("", 421, 0, 2, date, dif, 1, 1, legend, 0)
                reply.append(dif_o)
                reply.append(dif421_o)
                print("l segundo ")

        for month in range(1, 13):  # Itera sobre todos los meses del 1 al 12
            date = f'{current_year}-{month:02d}-28'
            process_dif(differences[month], a16_dict[month], date)

        a_dict = {account: {month: 0 for month in range(1, 13)} for account in [5, 6, 7, 8, 9, 10, 11]}

        return reply
