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
    username = request.form["username"].strip()
    password = request.form["password"].strip()
    user = login(username)
    errors = {}
    if(user["status"] == True):
        if(check_password_hash(user["password"], password)):
            session["id"] = user["userId"]
            session["user"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for('index'))
        else:
            errors["password"] = "your password is incorrect"
            return render_template('auth/login.html', errors=errors, username=username)
    else:
        errors["username-email"] = "your username or Email not found"
        return render_template('auth/login.html', errors=errors, username=username)


def logout():
    session.pop("user", '')
    session.pop("id", '')
    session.pop("role", '')
    return redirect(url_for('index'))
