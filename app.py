from flask import Flask
from flask_mysqldb import MySQL
from config.database import *

app=Flask(__name__)
app.config['MYSQL_HOST']= host
app.config['MYSQL_USER']= user
app.config['MYSQL_DB']= database    
app.config['SECRET_KEY'] = 'aaaa'

mysql=MySQL(app)

from controller.indexController import *
from controller.insertTransactionsController import *
from controller.reportsController import *
from controller.quickInsertController import *
from controller.exchangeController import *
from controller.graphicController import *
from models.errors import *

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

