
from models.transactions import Transactions
from config.conf import Inic

class Queries:   
    def InsertQuickTransac(transaction:Transactions) -> None:
        query ="""INSERT INTO accountingtransactions (FkidVAccount,FkidSubAccount,FkidVIncreasedBY
        ,accruedDate,amount,FKidCountry,FkidCity,comment,FkidDues) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
       
       # Diccionario para el mapeo de cuentas
        account_map = {
            "1": 341,
            "2": 331,
            "3": 333,
            "4": 17,
            "5": 342,
            "6": 304,
            "7": 305,
            "8": 301,
            "9": 306,
            "10": 307,
            "11": 311,
            "31": 1,
            "32": 210,
            "33": 212,
            "34": 211,
            "35": 213,
            "36": 13
        }

        # Obtener y mapear la cuenta
        account = transaction.getFkidVAccount()
        if account in account_map:
            transaction.setFkidVAccount(account_map[account])
        
        # Validar datos antes de la inserción
        try:
            parameters = [
                transaction.getFkidVAccount(),
                transaction.getFkidSubAccount(),
                transaction.getFkidVIncreasedBY(),
                transaction.getaccruedDate(),
                transaction.getamount(),
                transaction.getFKidCountry(),
                transaction.getFkidCity(),
                transaction.getcomment(),
                transaction.getFkidDues()
            ]

            # Verificar que todos los parámetros sean válidos
            for param in parameters:
                if param is None:
                    raise ValueError("Valor invalido")

            # Realizar la inserción en la base de datos
            Inic.db_insert(query, parameters)
        
        except Exception as e:
            # Manejar errores de inserción
            print(f"Error de inserción: {e}")
       
       
       
       
       
     