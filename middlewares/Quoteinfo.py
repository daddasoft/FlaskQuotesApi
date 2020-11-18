from flask import request, jsonify


def SetDefault(fun):
    def nestedFunc():
        data = request.get_json()
        if("body" not in data or len(data["body"]) < 5):
            return jsonify({"message": "Body Should Contain At Least 5 Characters",
                            "field": "body"}), 400
        if("category" not in data or len(data["category"]) < 2):
            data["category"] = "other"
        if("author" not in data or len(data["author"]) < 2):
            data["author"] = "Unknown"
        return fun()
    return nestedFunc
