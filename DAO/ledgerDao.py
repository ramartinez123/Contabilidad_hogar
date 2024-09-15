
from models.ledger import Ledger
from config.conf import Inic
from typing import List

# Consulta estandard a la base de datos para mayor
class Queries:   
    def build_query(year: int,inicio: int, fin:int, inicio2:int, fin2: int) -> list[Ledger]:
        return f"""
            SELECT accountingtransactions.FkidVAccount AS Codigo, accounts.account AS Cuenta,
            SUM(IF(accruedDate BETWEEN '{year}-01-01' AND '{year}-01-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-01-01' AND '{year}-01-31' AND FkidVIncreasedBY=2, amount, 0)) AS enero,
            SUM(IF(accruedDate BETWEEN '{year}-02-01' AND '{year}-02-28' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-02-01' AND '{year}-02-28' AND FkidVIncreasedBY=2, amount, 0)) AS febrero,
            SUM(IF(accruedDate BETWEEN '{year}-03-01' AND '{year}-03-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-03-01' AND '{year}-03-31' AND FkidVIncreasedBY=2, amount, 0)) AS marzo,
            SUM(IF(accruedDate BETWEEN '{year}-04-01' AND '{year}-04-30' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-04-01' AND '{year}-04-30' AND FkidVIncreasedBY=2, amount, 0)) AS abril,
            SUM(IF(accruedDate BETWEEN '{year}-05-01' AND '{year}-05-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-05-01' AND '{year}-05-31' AND FkidVIncreasedBY=2, amount, 0)) AS mayo,
            SUM(IF(accruedDate BETWEEN '{year}-06-01' AND '{year}-06-30' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-06-01' AND '{year}-06-30' AND FkidVIncreasedBY=2, amount, 0)) AS junio,
            SUM(IF(accruedDate BETWEEN '{year}-07-01' AND '{year}-07-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-07-01' AND '{year}-07-31' AND FkidVIncreasedBY=2, amount, 0)) AS julio,
            SUM(IF(accruedDate BETWEEN '{year}-08-01' AND '{year}-08-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-08-01' AND '{year}-08-31' AND FkidVIncreasedBY=2, amount, 0)) AS agosto,
            SUM(IF(accruedDate BETWEEN '{year}-09-01' AND '{year}-09-30' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-09-01' AND '{year}-09-30' AND FkidVIncreasedBY=2, amount, 0)) AS septiembre,
            SUM(IF(accruedDate BETWEEN '{year}-10-01' AND '{year}-10-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-10-01' AND '{year}-10-31' AND FkidVIncreasedBY=2, amount, 0)) AS octubre,
            SUM(IF(accruedDate BETWEEN '{year}-11-01' AND '{year}-11-30' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-11-01' AND '{year}-11-30' AND FkidVIncreasedBY=2, amount, 0)) AS noviembre,
            SUM(IF(accruedDate BETWEEN '{year}-12-01' AND '{year}-12-31' AND FkidVIncreasedBY=1, amount, 0)) -
            SUM(IF(accruedDate BETWEEN '{year}-12-01' AND '{year}-12-31' AND FkidVIncreasedBY=2, amount, 0)) AS diciembre
            FROM accountingtransactions
            INNER JOIN accounts ON accountingtransactions.FkidVAccount = accounts.idAccount
            WHERE accountingtransactions.FkidVAccount > {inicio} AND accountingtransactions.FkidVAccount < {fin} or accountingtransactions.FkidVAccount > {inicio2} AND accountingtransactions.FkidVAccount < {fin2}
            GROUP BY FkidVAccount
            ORDER BY FkidVAccount
    """

    # Procesos armado reporte para Perdidas y Gananacias
    def process_answers_A(answers, factor=1):
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = []
        for answer in answers:
            ledger = Ledger(answer[0], answer[1],
                            answer[2] * factor, answer[3] * factor, answer[4] * factor, answer[5] * factor,
                            answer[6] * factor, answer[7] * factor, answer[8] * factor, answer[9] * factor,
                            answer[10] * factor, answer[11] * factor, answer[12] * factor, answer[13] * factor)
            partialAcum = Ledger("", "Total",
                                 partialAcum.get_january() + ledger.get_january(), partialAcum.get_february() + ledger.get_february(),
                                 partialAcum.get_march() + ledger.get_march(), partialAcum.get_april() + ledger.get_april(),
                                 partialAcum.get_may() + ledger.get_may(), partialAcum.get_june() + ledger.get_june(),
                                 partialAcum.get_july() + ledger.get_july(), partialAcum.get_august() + ledger.get_august(),
                                 partialAcum.get_september() + ledger.get_september(), partialAcum.get_october() + ledger.get_october(),
                                 partialAcum.get_november() + ledger.get_november(), partialAcum.get_december() + ledger.get_december())
           
            records.append(ledger)
        records.append(partialAcum)
        return records   
    
    # Procesos armado reporte para Activo y Pasivo con valores mensuales acumulados
    def process_answers_B(answers, factor=1):
        partialAcum = Ledger("","",0,0,0,0,0,0,0,0,0,0,0,0) 
        records = []
        for answer in answers:
                answer = Ledger( answer[0],answer[1]
                             ,answer[2] * factor                                                
                             ,sum(answer[2:4]) * factor
                             ,sum(answer[2:5]) * factor
                             ,sum(answer[2:6]) * factor
                             ,sum(answer[2:7]) * factor
                             ,sum(answer[2:8]) * factor
                             ,sum(answer[2:9]) * factor
                             ,sum(answer[2:10]) * factor
                             ,sum(answer[2:11]) * factor
                             ,sum(answer[2:12]) * factor
                             ,sum(answer[2:13]) * factor
                             ,sum(answer[2:14]) * factor)
                partialAcum = Ledger("","Total",partialAcum.get_january() + answer.get_january(),partialAcum.get_february() + answer.get_february()
                                    ,partialAcum.get_march() + answer.get_march(),partialAcum.get_april() + answer.get_april()
                                    ,partialAcum.get_may() + answer.get_may(),partialAcum.get_june() + answer.get_june()
                                    ,partialAcum.get_july() + answer.get_july(),partialAcum.get_august() + answer.get_august()
                                    ,partialAcum.get_september() + answer.get_september(),partialAcum.get_october() + answer.get_october()
                                    ,partialAcum.get_november() + answer.get_november(),partialAcum.get_december() + answer.get_december())
                records.append(answer)
        records.append (partialAcum)      
        return records   

    #Reporte Perdidas
    def Losses_byYear(year: int) -> List[Ledger]:
        query = Queries.build_query(year, 301, 400, 301, 400)
        parameters =[]
        answers = Inic.db_connect(query,parameters)
        return Queries.process_answers_A(answers, factor=1)
    
    #Reporte Ganancias
    def Profits_byYear(year: int) -> List[Ledger]: 
        query = Queries.build_query(year, 401, 400, 401, 500)
        parameters =[]
        answers = Inic.db_connect(query,parameters)
        return Queries.process_answers_A(answers, factor=-1)

    #Reporte Activo
    def Assets_byYear(year: int) -> List[Ledger]:        
        query = Queries.build_query(year,0,5,14,100)
        parameters =[]
        answers = Inic.db_connect(query,parameters)
        return Queries.process_answers_B(answers, factor=1)
  
    #Reporte Pasivo
    def Liabilities_byYear(year: int) -> List[Ledger]: 
        query = Queries.build_query(year,201,300,201,300)
        parameters =[]
        answers = Inic.db_connect(query,parameters)
        return Queries.process_answers_B(answers, factor=-1)

    #Reporte Activo Moneda Extranjera
    def Assets_byYear_D(year: int) -> List[Ledger]: 
        query = Queries.build_query(year,4,12,4,12)
        parameters =[]
        answers = Inic.db_connect(query,parameters)
        return Queries.process_answers_B(answers, factor=-1)
       