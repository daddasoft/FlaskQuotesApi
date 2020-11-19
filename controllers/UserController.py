from flask import request, render_template
from flask.globals import session
from flask.helpers import url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from models.User import login, store
from middlewares.userLogin import LoginValidator
from middlewares.UserRegister import RegisterValidator


@RegisterValidator
def create():
    username = request.form["username"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    if(store(username, email, password)):
        return redirect(url_for('index'))
    return render_template('auth/register.html')


@LoginValidator
def log():
    username = request.form["username"]
    password = request.form["password"]
    user = login(username)
    if(user["status"] == True):
        if(check_password_hash(user["password"], password)):
            session["id"] = user["userId"]
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for('index'))
        else:
            print("Invalid Password")
            return render_template('auth/login.html')
    else:
        print(user["message"])
        return render_template('auth/login.html')
