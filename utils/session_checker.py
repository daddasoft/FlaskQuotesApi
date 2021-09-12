from flask import session
from flask.helpers import url_for
from werkzeug.utils import redirect


def session_check():
    if("user" in session):
        return redirect(url_for('index'))
