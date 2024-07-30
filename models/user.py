from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name 
        self.password = password

    def getidUser(self):
        return self.id

    def setidUser(self,value):
        self.user =value

    def getnameUser(self):
        return self.name

    def setnameUser(self,value):
        self.name =value

    def getpasswordUser(self):
        return self.password

    def setpasswordUser(self,value):
        self.password =value


    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)
 
