from flask import Flask, jsonify, render_template, session, redirect, url_for
from flask_cors import CORS
from config.env import env
from controllers import QuoteController as Quote
from controllers import UserController as User
QuotesApp = Flask(__name__)
QuotesApp.config['SECRET_KEY'] = env("appSecret")
CORS(QuotesApp)


@QuotesApp.route("/")
def index():
    return Quote.homeIndex()


@QuotesApp.route("/api/quotes", methods=["POST"])
def create():
    return Quote.store()


@QuotesApp.route("/api/quotes/<id>", methods=["DELETE"])
def delete(id):
    return Quote.delete(id)


@QuotesApp.route("/api/quotes/random",)
def randomQ():
    return Quote.randomize()


@QuotesApp.route("/api/quotes/<id>", methods=["DELETE"])
def apiDelete(id):
    if("authorization" not in request.headers):
        return jsonify({"msg": "Unauthorized"}), 401
    try:
        decoded = jwt.decode(
            request.headers["authorization"], env("JWT_SECRET"))
        userID = decoded["userId"]
    except:
        return jsonify({"msg": "Invalid / Expaired Token"}), 400
    if(Quote.Quote.destroy(id, userID) == 1):
        return jsonify([]), 200
    return jsonify({"error": "can't Delete this Quote"})
def getQuotes():
    data = Quote.index()
    if("message" not in data and len(data) != 0):
        return jsonify(data), 200
    return jsonify(data), 404


@QuotesApp.route("/register")
def register():
    if("user" in session):
        return redirect(url_for('index'))
    return render_template('auth/register.html', title="Register")


@QuotesApp.route("/register", methods=["POST"])
def registerPost():
    return User.create()


@QuotesApp.route("/login", methods=["POST"])
def loginPost():
    return User.log()


@QuotesApp.route("/login")
def login():
    if("user" in session):
        return redirect(url_for('index'))
    return render_template('auth/login.html', title="Login")


@QuotesApp.route("/logout")
def logoutGet():
    return redirect(url_for('index'))


@QuotesApp.route("/logout", methods=["POST"])
def logout():
    return User.logout()


if(__name__ == "__main__"):
    QuotesApp.run()
