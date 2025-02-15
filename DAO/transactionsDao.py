from models.transactions import Transactions
from models.transactions import Transactions
from config.conf import Inic
from helpers.useful import Exchanges
import logging
from datetime import datetime
from flask import flash

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Queries:   

    """def validate_transaction(transaction: Transactions) -> bool:

        if not transaction.getFkidVAccount():
           logging.error("La cuenta no puede estar vacía.")
           return False    

        if not transaction.getaccruedDate():
           logging.error("La fecha no puede estar vacía.")
           return False
       
        try:
            datetime.strptime(accrued_date, "%Y-%m-%d")
        except ValueError:
            logging.error("La fecha debe estar en formato YYYY-MM-DD.")
            return False"""
        
    def QueryTransaction() -> list[Transactions]:  
        query ="""SELECT accountingtransactions.*,accounts.account FROM accountingtransactions 
        INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount
        ORDER BY accountingtransactions.idAccountingTransaction ASC"""
        parameters=[]
        try:
            answers = Inic.db_connect(query,parameters)
            records = []    
            for answer in answers:
                 answer = Transactions( answer[0],answer[10],answer[2],answer[3],answer[4]
                                       ,answer[5],answer[6],answer[7],answer[8],answer[9])
                 records.append(answer)
            return records 
        except Exception as e:
            print(f"No se recibieron datos: {e}")
            return records
            
    def InsertTransaction(transaction:Transactions) -> None:
        # Validar la transacción antes de la inserción
        """if not Queries.validate_transaction(transaction):
            logging.error("Transacción inválida, no se insertará.")
            return"""
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY,accruedDate
        ,amount,FKidCountry,FkidCity,comment,FkidDues)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        parameters=[transaction.get_fkid_v_account(),
                transaction.get_fkid_sub_account(),
                transaction.get_fkid_v_increased_by(),
                transaction.get_accrued_date(),
                transaction.get_amount(),   
                transaction.get_fkid_country(),
                transaction.get_fkid_city(),
                transaction.get_comment(),
                transaction.get_fkid_dues()] 
        try:          
            Inic.db_insert(query,parameters)    
        except Exception as e:
            print(f"Error insertando datos: {e}") 

    def QuerybyDate(transaction:Transactions) -> list[Transactions]: 
        query ="""SELECT accountingtransactions.*,accounts.account FROM accountingtransactions INNER JOIN accounts on accountingtransactions.FkidVAccount=accounts.idAccount
        where accountingtransactions.accruedDate = (%s) """ 
        parameters=[transaction.getaccruedDate()]
        try:
            answers = Inic.db_connect(query,parameters)
            records = []
            for answer in answers:
                answer = Transactions( answer[0],answer[10],answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9])
                records.append(answer)
            return records 
        except Exception as e:
            print(f"No se recibieron datos: {e}")
            return []
    
    def InsertExchange() -> None:
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY,accruedDate
        ,amount,FKidCountry,FkidCity,comment,FkidDues)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        transactions=Exchanges.UpdateExchange()
        for transaction in transactions:
          parameters=[transaction.get_fkid_v_account(),transaction.get_fkid_sub_account(),
                    transaction.get_fkid_v_increased_by(),transaction.get_accrued_date(),transaction.get_amount(),
                    transaction.get_fkid_country(),
                    transaction.get_fkid_city(),transaction.get_comment(),transaction.get_fkid_dues()  ] 
          try:       
              Inic.db_insert(query,parameters) 
          except Exception as e:
              print(f"Error insertando datos: {e}") 

    # Valida los datos de la transacción antes de la inserción.
