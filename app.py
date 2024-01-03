from flask import Flask
from flask_mysqldb import MySQL
from config.database import *
from flask_login import LoginManager
import unittest

app=Flask(__name__)
app.config['MYSQL_HOST']= host
app.config['MYSQL_USER']= user
app.config['MYSQL_DB']= database    
app.config['SECRET_KEY'] = 'aaaa'

mysql=MySQL(app)
login_manager = LoginManager(app)

from controller.indexController import *
from controller.transactionsController import *
from controller.ledgerController import *
from controller.quickTransactionController import *
from controller.exchangeController import *
from controller.graphicController import *
from controller.loginController import *
from controller.accountController import *
from models.errors import *

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

