from config.database import connect
from utils.toDictionary import ToDictionary
from utils.PaginationCreator import PgCreator


def get():
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute("SELECT * FROM quotes order by createdAt DESC")
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


def destroy(id, userId):
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(
            "DELETE  FROM quotes WHERE id=%s and createdBy = %s", (id, userId))
        database.commit()
        if(cursor.rowcount > 0):
            return 1
        return -1
    except:
        return 0


def paginate(page=1):
    try:
        database = connect()
        cursor = database.cursor()
        OFFSET = abs(5 * (int(page)-1))
        cursor.execute(
            f"SELECT * FROM quotes order by createdAt DESC LIMIT 5 OFFSET {OFFSET}")
        result = cursor.fetchall()
        cursor.execute(f"SELECT COUNT(*) FROM quotes")
        res2 = cursor.fetchone()
        resultByPG = PgCreator(res2[0], page, 5)
        resultByPG["data"] = ToDictionary(result)
        database.commit()
        return resultByPG
    except:
        return {"message": "can't find any Quote"}


def paginateforHome(page=1):
    try:
        database = connect()
        cursor = database.cursor()
        OFFSET = abs(5 * (int(page)-1))
        cursor.execute(
            f"SELECT * FROM quotes order by createdAt DESC LIMIT  5 OFFSET {OFFSET}")
        result = cursor.fetchall()
        cursor.execute(f"SELECT COUNT(*) FROM quotes")
        res2 = cursor.fetchone()
        result = {"data": result, "count": res2[0]}
        database.commit()
        return result
    except:
        return {"message": "can't find any Quote"}


def random():
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(
            "SELECT body,author,category FROM quotes ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        database.commit()
        if(cursor.rowcount > 0):
            return {"body": result[0], "author": result[1], "category": result[2]}
        return {"message": "can't find any Quote"}
    except:
        return {"message": "Error for find any Quote"}


def archive(id):
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(
            f"SELECT q.id,q.category,q.author,q.body,q.createdAt FROM quotes q WHERE q.createdBy =%s", (id,))
        res = cursor.fetchall()
        database.commit()
        if(cursor.rowcount > 0):
            return res
        return None
    except:
        return None
