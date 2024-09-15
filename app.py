from flask import Flask
from flask_mysqldb import MySQL
from config.database import *
from flask_login import LoginManager
import logging
import unittest


logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicialización de la aplicación Flask
app=Flask(__name__)
app.config['MYSQL_HOST']= host
app.config['MYSQL_USER']= user
app.config['MYSQL_DB']= database    
app.config['SECRET_KEY'] = 'aaaa'

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

#Inicialización de MySQL y LoginManager:
try:
    mysql = MySQL(app)
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

try:
    login_manager = LoginManager(app)
except Exception as e:
    print(f"Error al inicializar el LoginManager: {e}")   

#Importación de Controladores y Modelos:
from controller.indexController import *
from controller.transactionsController import *
from controller.ledgerController import *
from controller.quickTransactionController import *
from controller.exchangeController import *
from controller.graphicController import *
from controller.loginController import *
from controller.accountController import *
from models.errors import *

#Ejecución de la Aplicación:
if __name__ == '__main__':
    app.run(port = 3000, debug = True)

