
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
        account = transaction.get_fkid_v_account()
        if account in account_map:
            transaction.set_fkid_v_account(account_map[account])
        
        # Validar datos antes de la inserción
        try:
            parameters = [
                transaction.get_fkid_v_account(),
                transaction.get_fkid_sub_account(),
                transaction.get_fkid_v_increased_by(),
                transaction.get_accrued_date(),
                transaction.get_amount(),   
                transaction.get_fkid_country(),
                transaction.get_fkid_city(),
                transaction.get_comment(),
                transaction.get_fkid_dues()
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
       
       
       
       
       
     