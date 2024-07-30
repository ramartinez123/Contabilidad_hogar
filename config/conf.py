from app import mysql

class Inic:
    @staticmethod
    def db_connect(query,parameters):      
       #  Ejecuta una consulta SELECT en la base de datos y devuelve los resultados. 
        try:    
           cur = mysql.connection.cursor()
           try:  
                 cur.execute(query,parameters) 
                 answer=cur.fetchall()
           except Exception as e:
                 print(f"Error de acceso a los datos: {e}")
           finally:
                cur.close()
        except:
           print("No se puedo establecer la conexion")  
           answer = None          
        return answer

    @staticmethod
    def db_insert(query,parameters):
        #  Ejecuta una consulta INSERT en la base de datos.
        try:
            cur = mysql.connection.cursor()
            try:  
                cur.execute(query,parameters) 
                mysql.connection.commit()  
            except Exception as e:
                print(f"Error de acceso a los datos: {e}")
            finally:
                cur.close()
        except Exception as e:
            print(f"No se pudo establecer la conexión: {e}")


      

        

        

