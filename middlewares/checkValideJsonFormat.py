from flask import request
from flask.json import jsonify


def CheckJson(fun):
    def nestedFunc():
        try:
            len(request.get_json())
        except:
            return jsonify({"message": "Make Sure You Have a valid Json Format"}), 400
        return fun()
    return nestedFunc
