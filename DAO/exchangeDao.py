
from models.exchange import Exchange
from config.conf import Inic

class Exchanges:   
    def InsertExchange(exchange:Exchange) -> Exchange:
        query ="INSERT INTO exchange (dateCoti,FKidCurrency,ImporteCot) VALUES(%s,%s,%s)"
        parameters=[exchange.getdateCoti(),exchange.getFkidCurrency(),exchange.getImporteCot()]    
        Inic.db_insert(query,parameters)    
 
    def QueryExchange() -> list[Exchange]:  
        query ="SELECT * FROM exchange " 
        parameters=[]
        answers = Inic.db_connect(query,parameters)
        records = []
        for answer in answers:
            answer = Exchange( answer[0],answer[1],answer[2],answer[3])
            records.append(answer)
        return records 