from flask import Flask, jsonify, request, escape
from config.env import env
from controllers import QuoteController as Quote
from models.Quote import destroy


QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")


@QuotesApp.route("/")
def index():
    return "Hello"


@QuotesApp.route("/quotes", methods=["POST"])
def create():
    return Quote.store()


@QuotesApp.route("/quotes/<id>", methods=["DELETE"])
def delete(id):
    return Quote.delete(id)


@QuotesApp.route("/quotes",)
def getQuotes():
    data = Quote.get()
    if("message" not in data and len(data) != 0):
        return jsonify(data), 200
    return jsonify(data), 404


if(__name__ == "__main__"):
    QuotesApp.run(port=5000, debug=True)
