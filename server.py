from flask import Flask, jsonify, request
from config.env import env
QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")


@QuotesApp.route("/")
# @deco
def index():
    return "Index"


@QuotesApp.route("/quotes", methods=["POST"])
def create():
    return "Add Quotes API KEY REQUIRED"


@QuotesApp.route("/quotes",)
def get():
    return "Get All Quotes Pagination Included"


if(__name__ == "__main__"):
    QuotesApp.run(port=5000, debug=True)
