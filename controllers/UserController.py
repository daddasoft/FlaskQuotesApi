from env import env
from flask.json import jsonify
from flask.json.tag import PassDict
from utils.session_checker import session_check
from flask import request, render_template
from flask.globals import session
from flask.helpers import url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect
from models.User import login, store
from middlewares.userLogin import LoginValidator
from middlewares.UserRegister import RegisterValidator
import re
from models.User import checkAvailableEmail, checkAvailableUsername, login, getUserPassword, change_password as ch
import jwt


@RegisterValidator
def create():
    session_check()
    username = request.form["username"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    if(store(username, email, password)):
        return render_template('auth/login.html', username=username, message="Account Created Successfully")
    return render_template('auth/register.html', title="quotes | register")


@LoginValidator
def log():
    session_check()
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
        return render_template('auth/login.html', errors=errors, username=username, title="quotes | login")


def logout():
    session_check()
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


def api_register():
    data = request.get_json()
    errors = {}
    # username Validation
    if("username" not in data or not re.search("^[a-z]+([0-9]+)?$", data["username"])):
        errors["username"] = "Username is not Valid should have (small letter & no Spaces)"
    elif (len(data["username"]) < 6 or len(data["username"]) > 15):
        errors["username"] = "Username Should be between 6 and 15 Characters"
    else:
        if(checkAvailableUsername(data["username"].strip())):
            errors["username"] = "There is a user with this Username"
    # Email Validation
    if("email" not in data or not re.search("[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", data["email"])):
        errors["email"] = "email is not Valid"
    elif (len(data["email"]) > 25):
        errors["email"] = "email is too Long"
    else:
        if(checkAvailableEmail(data["email"])):
            errors["email"] = "email is Already Exist"
    # username Password
    if("password" not in data or len(data["password"].strip()) < 6 or len(data["password"].strip()) > 20):
        errors["password"] = "password should contain between 6 and 20 characters"
    if("password-confirm" not in data or data["password-confirm"] != data["password"]):
        errors["password-confirm"] = "Confirm Password not valid"
    if(errors):
        return jsonify(errors), 400
    else:
        password = generate_password_hash(data["password"])
        if(store(data["username"], data["email"], password)):
            return api_login({"username": data["username"], "password": data["password"]})
        return jsonify({"message": "can't create a user"}), 500


def change_password():
    password = request.form.get("password")
    new_password = request.form.get("new-password")
    confirm_new_password = request.form.get("confirm-new-password")
    errors = {}
    if(len(password) < 5):
        errors["password"] = "password is too short"
    if (len(new_password) < 5):
        errors["new-password"] = "new password is too short"
    if (new_password != confirm_new_password):
        errors["confirm-new-password"] = "confirm new passwords not match"
    if(len(errors) > 0):
        return render_template("auth/change-password.html", errors=errors, title="quotes | change password")
    user_password = getUserPassword(session["id"])
    if(check_password_hash(user_password, password)):
        hashed_pass = generate_password_hash(new_password)
        if(not ch(hashed_pass, session["id"])):
            errors["password"] = "can't change password "
        else:
            return render_template("auth/change-password.html", errors=errors, message="password changed", title="quotes | change password")
    else:
        errors["password"] = "current password incorrect"
    return render_template("auth/change-password.html", errors=errors, title="quotes | change password")
