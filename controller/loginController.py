from flask import render_template,request,redirect,url_for,flash
from app import app
from models.login import NameForm
from models.user import User
from flask_login import logout_user, LoginManager,login_user,current_user
from DAO.userDAO import Usera

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(id):
    answer=Usera.load_user_DAO(id)
    return answer

@app.route('/login2',methods=['GET', 'POST'])
def login2():
    form=NameForm()
    
    if form.validate_on_submit():
        user= User(0,form.name.data,form.password.data)
        logged_user=Usera.QueryUser(user) 
        if logged_user is not None :
            if logged_user.password: 
                login_user(logged_user)
                return redirect("home")
            else:
                return redirect(url_for("login"))
        else:           
            return redirect(url_for("login"))     
    else:           
        return render_template("login2.html",form=form)  


@app.route('/logout')    
def logout():
    logout_user()
    return redirect(url_for("login2"))


@app.route('/login')
def login():
    return render_template("login.html") 




    
    


