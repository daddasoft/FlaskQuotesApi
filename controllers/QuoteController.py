from flask.json import jsonify
from models.Quote import get, paginate
from flask import request


def index():
    return get()
