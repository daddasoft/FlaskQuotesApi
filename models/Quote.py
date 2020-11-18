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


def create(body, author, createdBy, category):
    try:
        database = connect()
        cursor = database.cursor()
        sql = "INSERT INTO `quotes` \
            ( `body`, `author`, `createdBy`, `category`, \
            `createdAt`, `updatedAt`) VALUES (%s,%s,%s,%s,CURRENT_TIMESTAMP(),CURRENT_TIMESTAMP())"
        cursor.execute(sql, (body, author, createdBy, category))
        lastID = cursor.getlastrowid()
        res = cursor.execute("SELECT * FROM quotes WHERE id =%s ", (lastID,))
        res = cursor.fetchall()
        database.commit()
        return {"status": True, "data": ToDictionary(res)}
    except:
        return {"status": False, "message": "Can't add a New Quote ", "code": "ex02"}


def paginate():
    pass
