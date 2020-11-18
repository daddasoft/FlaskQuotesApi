from flask import Flask, jsonify, request
from config.env import env
from controllers import QuoteController as Quote
from models.Quote import create as QuoteCreate
QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")


@QuotesApp.route("/")
# @deco
def index():
    return "Hello"


@QuotesApp.route("/quotes", methods=["POST"])
def create():
    data = request.get_json()
    body = data["body"]
    category = data["category"]
    createdBy = data["createdBy"]
    author = data["author"]
    createQuote = QuoteCreate(body, author, createdBy, category)
    if(createQuote["status"]):
        return jsonify(createQuote["data"]), 201
    return jsonify(createQuote["message"]), 400


@QuotesApp.route("/quotes",)
def getQuotes():
    data = Quote.get()
    if("message" not in data):
        return jsonify(data), 200
    return jsonify(data), 404


if(__name__ == "__main__"):
    QuotesApp.run(port=5000, debug=True)
