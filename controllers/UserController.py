from flask import request, render_template
from flask.helpers import url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from models.User import store

from middlewares.UserRegister import RegisterValidator


@RegisterValidator
def create():
    username = request.form["username"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])
    if(store(username, email, password)):
        return redirect(url_for('index'))
    return render_template('auth/register.html')
