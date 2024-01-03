from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name 
        self.password = password

    def getidUser(self):
        return self.id

    def setidUser(self,x):
        self.user =x

    def getnameUser(self):
        return self.name

    def setnameUser(self,x):
        self.name =x

    def getpasswordUser(self):
        return self.password

    def setpasswordUser(self,x):
        self.password =x


    @classmethod
    def check_password(self,hashed_password,password):
        return check_password_hash(hashed_password,password)
 
