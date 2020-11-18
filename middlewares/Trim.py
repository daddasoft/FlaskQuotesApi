from flask import request


def Trim(fun):
    def nestedFunc():
        if(len(request.get_json()) > 0):
            for key, value in request.get_json().items():
                request.get_json()[key] = value.strip()
        return fun()
    return nestedFunc
