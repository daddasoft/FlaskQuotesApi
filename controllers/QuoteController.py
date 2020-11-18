from models import Quote
from flask import request, jsonify
from middlewares.Quoteinfo import SetDefault
from middlewares.Trim import Trim
from middlewares.checkValideJsonFormat import CheckJson


def index():
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
