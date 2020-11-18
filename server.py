from flask import Flask, jsonify, request
from config.env import env
from controllers import QuoteController as Quote
QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")


@QuotesApp.route("/")
# @deco
def index():
    data = Quote.get()
    if("message" not in data):
        return jsonify(data), 200
    return jsonify(data), 404


@QuotesApp.route("/quotes", methods=["POST"])
def create():
    return "Add Quotes API KEY REQUIRED"


@QuotesApp.route("/quotes",)
def getQuotes():
    return "Get All Quotes Pagination Included"


if(__name__ == "__main__"):
    QuotesApp.run(port=5000, debug=True)
