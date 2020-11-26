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
    if("user" in session):
        return redirect(url_for('index'))
    username = request.form["username"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    if(store(username, email, password)):
        return render_template('auth/login.html', username=username, message="Account Created Successfully")
    return render_template('auth/register.html')


@LoginValidator
def log():
    if("user" in session):
        return redirect(url_for('index'))
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
    if("user" not in session):
        return redirect(url_for('login'))
    session.pop("user", '')
    session.pop("id", '')
    session.pop("role", '')
    return redirect(url_for('index'))

def api_login(info):
    data = (info or request.get_json())
    if(not data):
        return jsonify({"msg": "Please Provide a username and password"}), 400
    if("username" not in data):
        return jsonify({"msg": "Please Provide a username"}), 400
    if("password" not in data):
        return jsonify({"msg": "Please Provide a password"}), 400
    username = data["username"]
    password = data["password"]
    userLogin = login(username)
    if(userLogin["status"] == True):
        if(check_password_hash(userLogin["password"], password)):
            token = jwt.encode(payload={"userId": userLogin["userId"],
                                        "username": userLogin["username"]}, key=env("JWT_SECRET"))
            return jsonify({"token": token}), 200

        else:
            return jsonify({"password": "Password is Incorrect"}), 400
    else:
        return jsonify({"usename": "user not Found"}), 400
