
from flask import request
from flask.templating import render_template


def LoginValidator(fun):
    def nestedFunc():
        data = request.form
        errors = {}
        if("username" not in data or len(data["username"]) < 6):
            errors["username"] = "Username Should at least contains 6 characters"
        if("password" not in data or len(data["password"]) < 6):
            errors["password"] = "password Should at least contains 6 characters"
        if(errors):
            username = data["username"] if "username" in data else ""
            return render_template("auth/login.html", errors=errors, username=username)
        return fun()
    return nestedFunc
