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
@QuotesApp.route("/api/quotes", methods=["POST"])
def apiStore():
    if("authorization" not in request.headers):
        return jsonify({"msg": "Unauthorized"}), 401
    token = str(request.headers["authorization"]).strip().split("Bearer ")[-1]
    try:
        decoded = jwt.decode(
            token, key=env("JWT_SECRET"), algorithms="HS256")
        userID = decoded["userId"]
    except Exception as v:
        return jsonify({"msg": "Invalid / Expaired Token"}), 400

    data = request.get_json()
    if(not data):
        return jsonify({"msg": "Please Provide a Quote Text"}), 400
    if("body" not in data or len(data["body"]) < 5):
        return jsonify({"body": "Please Provide a body for the Quote and have at least 5 characters"}), 400
    if("author" not in data or len(data["author"].strip()) < 3):
        data["author"] = 'Unknown'
    if("category" not in data or len(data["category"].strip()) < 3):
        data["category"] = 'other'
    res = Quote.Quote.create(
        data["body"], data["author"], userID, data["category"])
    if(res["status"]):
        return jsonify(res["data"][0]), 200
    return jsonify(res), 400
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
