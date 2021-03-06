from math import ceil
from flask.globals import session
from flask.templating import render_template
from middlewares.Auth import isAuth
from models import Quote
from flask import request, jsonify
from middlewares.Quoteinfo import SetDefault
from middlewares.Trim import Trim
from middlewares.checkValideJsonFormat import CheckJson
from middlewares.isTheOwner import checkOwner
from models.Quote import paginateforHome
from models.Quote import random


def index():
    page = request.args.get("page")
    if (page):
        return Quote.paginate(page)
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
    data = paginateforHome(page)
    if("message" in data):
        return render_template("index.html")
    totalPages = ceil(data["count"]/5)
    return render_template("index.html", data=data, total=int(totalPages), current=int(page), dataCount=len(data["data"]))


def randomize():
    data = random()
    if("message" in data):
        return jsonify(data), 400
    return jsonify(data), 200
