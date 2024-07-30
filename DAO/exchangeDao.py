
from models.exchange import Exchange
from config.conf import Inic

class Exchanges:   
    def InsertExchange(exchange:Exchange) -> None:
        query ="INSERT INTO exchange (dateCoti,FKidCurrency,ImporteCot) VALUES(%s,%s,%s)"
        parameters=[exchange.getdateCoti(),exchange.getFkidCurrency(),exchange.getImporteCot()]  

        # Validación de datos antes de la inserción
        for param in parameters:
            if param is None:
                raise ValueError("Parametro invalido")

        try:
            Inic.db_insert(query, parameters)
        except Exception as e:
            # Manejo de errores durante la inserción
            print(f"Error insertando datos: {e}")  

 
    def QueryExchange() -> list[Exchange]:  
        query ="SELECT * FROM exchange " 
        parameters=[]

        try:
            answers = Inic.db_connect(query,parameters)
            records = []
            for answer in answers:
                answer = Exchange( answer[0],answer[1],answer[2],answer[3])
                records.append(answer)
            return records 
        
        except Exception as e:
        # Manejo de errores durante la consulta
            print(f"No se recibieron dato: {e}")
            return []