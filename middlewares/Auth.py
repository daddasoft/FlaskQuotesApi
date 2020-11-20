from flask import session
from flask.helpers import url_for
from flask.json import jsonify
from werkzeug.utils import redirect


def isAuth(fun):
    def nestedFunc(*args):
        if("user" not in session):
            return jsonify({"message": "You are not logged in to perform this action"}), 401
        return fun(*args)
    return nestedFunc
