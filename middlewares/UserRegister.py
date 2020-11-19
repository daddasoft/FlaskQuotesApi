from re import error
from flask import request, jsonify
import re
from models.User import checkAvailableEmail, checkAvailableUsername
from flask.templating import render_template


def RegisterValidator(fun):
    def nestedFunc():
        data = request.form
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
            return render_template('auth/register.html', errors=errors, email=data["email"], username=data["username"])
        return fun()
    return nestedFunc
