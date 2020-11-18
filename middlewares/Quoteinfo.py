from flask import request, jsonify


def SetDefault(fun):
    def nestedFunc():
        data = request.get_json()
        if("body" not in data):
            return jsonify({"message": "Body Should Contain At Least 5 Characters",
                            "field": "body"}), 400
        if("category" not in data):
            data["category"] = "other"
        if("author" not in data):
            data["author"] = "Unknown"
        return fun()
    return nestedFunc
