from flask import session
from flask.json import jsonify
from config.database import connect


def checkOwner(QuoteId):
    try:
        database = connect()
        userId = session["id"]
        cursor = database.cursor()
        sql = f"SELECT id FROM quotes WHERE id= %s and createdBy =%s"
        cursor.execute(sql, (userId, QuoteId))
        cursor.fetchone()
        database.commit()
        if(cursor.rowcount > 0):
            return True
        return False
    except:
        return False


def ownerValidator(fun):
    def nestedFunc(id):
        if(not checkOwner(id)):
            return jsonify({"message": "You are not the owner of this quote"})
        return fun()
    return nestedFunc
