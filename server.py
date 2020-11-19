from flask import Flask, jsonify, request, escape, render_template, session
from flask_cors import CORS
from config.env import env
from controllers import QuoteController as Quote
from models.Quote import destroy
from controllers import UserController as User

QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")
CORS(QuotesApp)


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
    data = Quote.index()
    if("message" not in data and len(data) != 0):
        return jsonify(data), 200
    return jsonify(data), 404


@QuotesApp.route("/register",)
def register():
    return render_template('auth/register.html', title="Register")


@QuotesApp.route("/register", methods=["POST"])
def registerPost():
    return User.create()


@QuotesApp.route("/login",)
def login():
    return render_template('auth/login.html', title="Login")


if(__name__ == "__main__"):
    QuotesApp.run(port=5000, debug=True)
