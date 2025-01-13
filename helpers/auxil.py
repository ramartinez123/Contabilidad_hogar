from models.exchange import Exchange
from config.conf import Inic
from datetime import datetime

current_year = datetime.now().year

class Exchangesa:    
        
    @staticmethod
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
   
    @staticmethod
    def importIs(importa) -> list[Exchange]: 
        curra = Exchangesa.Todayis(importa)
        start_date= datetime(current_year - 1, 12, 31).strftime('%Y-%m-%d')
        parameters=[start_date,curra]
        query24 ="""SELECT MONTH (dateCoti) as mes, dateCoti, FKidCurrency, ImporteCot 
                    from exchange 
                    WHERE dateCoti > %s 
                    and dateCoti in (SELECT MAX(dateCoti) 
                                    from exchange
                                    GROUP BY MONTH (dateCoti), FKidCurrency) 
                    and FKidCurrency = %s"""

        records =[]
        answers = Inic.db_connect(query24,parameters)     
        records = [Exchange(*answer) for answer in answers]       
        return records
    
    #@app.template_filter('format_currency')
    def format_currency(value):
        try:
        # Formato sin decimales, con separador de miles
            return f"${int(value):,}".replace(",", ".")
        except (ValueError, TypeError):
            return value  # Devuelve el valor original en caso de error