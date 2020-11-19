from flask import request, render_template
from werkzeug.security import generate_password_hash


def create():
    username = request.form["username"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    confirmPassword = request.form["password-confirm"]
    print(username, email, password, confirmPassword)
    return render_template('auth/register.html')
