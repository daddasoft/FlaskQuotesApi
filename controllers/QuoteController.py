from math import ceil
from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from middlewares.Auth import isAuth
from models import Quote
from flask import request, jsonify
from middlewares.Quoteinfo import SetDefault
from middlewares.Trim import Trim
from middlewares.checkValideJsonFormat import CheckJson
from middlewares.isTheOwner import checkOwner
from models.Quote import paginateforHome, archive
from models.Quote import random
from env import env
from werkzeug.security import generate_password_hash


def index():
    page = request.args.get("page")
    limit = request.args.get("limit")
    if (page):
        return Quote.paginate(page=page, limit=limit or (env("paginate") or 5))
    return Quote.get()


@CheckJson
@Trim
@SetDefault
def store():
    if("user" not in session):
        return jsonify({"message": "you Should be logged in"}), 401
    data = request.get_json()
    body = data["body"]
    category = data["category"]
    createdBy = session["id"]
    author = data["author"]
    createQuote = Quote.create(body, author, createdBy, category)
    if(createQuote["status"]):
        return jsonify(createQuote["data"]), 201
    return jsonify({"message": createQuote["message"]}), 400


@isAuth
def delete(id):
    res = Quote.destroy(id, session["id"])
    if(res > 0):
        return jsonify([]), 200
    elif (res < 0):
        return jsonify({"message": "quote not found may it already deleted"}), 404
    else:
        return jsonify({"message": "quote can't be deleted"}), 400


def homeIndex():
    page = request.args["page"] if "page" in request.args else 1
    limit = request.args.get("limit") or (env("paginate") or 5)
    data = paginateforHome(page=page, limit=limit)
    if("message" in data):
        return render_template("index.html", title="quotes | home")
    totalPages = ceil(data["count"]/(int(env("paginate") or 5)))
    return render_template("index.html", title="quotes | home", data=data, total=int(totalPages), current=int(page), dataCount=len(data["data"]))


def randomize():
    data = random()
    if("message" in data):
        return jsonify(data), 400
    return jsonify(data), 200


def get_archive():
    return archive(session["id"])
