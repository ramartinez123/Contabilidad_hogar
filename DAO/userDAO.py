from app import login_manager
from models.user import User
from config.conf import Inic

class Usera:  

    @classmethod
    def QueryUser(self,user:User) -> User: 
        query ="SELECT * FROM user WHERE name =(%s)"
        parameters=[user.getnameUser()]
        aux=user.password
        answerx = Inic.db_connect(query,parameters)
        nn=answerx[0][2]
        answery=User(answerx[0][0],answerx[0][1],User.check_password(nn,aux))
        return answery  

    
    @login_manager.user_loader
    def load_user_DAO(id):
        query ="SELECT * FROM user WHERE id =(%s)"
        parameters=id
        answerx1 = Inic.db_connect(query,parameters)
        user_logged=User(answerx1[0][0],answerx1[0][1],answerx1[0][2])
        return user_logged

    
