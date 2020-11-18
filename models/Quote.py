from config.database import connect
from utils.toDictionary import ToDictionary


def get():
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute("SELECT * FROM quotes")
        result = cursor.fetchall()
        result = ToDictionary(result)
        database.commit()
        return result
    except:
        return {"message": "can't find any Quote"}


def paginate():
    pass
