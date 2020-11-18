from models import Quote
from flask import request, jsonify
from middlewares.Quoteinfo import SetDefault
from middlewares.Trim import Trim
from middlewares.checkValideJsonFormat import CheckJson


def index():
    page = request.args.get("page")
    if (page):
        return Quote.paginate(page)
    return Quote.get()


@CheckJson
@Trim
@SetDefault
def store():
    data = request.get_json()
    body = data["body"]
    category = data["category"]
    createdBy = 8
    author = data["author"]
    createQuote = Quote.create(body, author, createdBy, category)
    if(createQuote["status"]):
        return jsonify(createQuote["data"]), 201
    return jsonify({"message": createQuote["message"]}), 400


def delete(id):
    res = Quote.destroy(id)
    if(res > 0):
        return jsonify([]), 200
    elif (res < 0):
        return jsonify({"message": "quote not found may it already deleted"}), 404
    else:
        return jsonify({"message": "quote can't be deleted"}), 400
