from config.database import connect


def store(username, email, password, role="user"):
    try:
        database = connect()
        cursor = database.cursor()
        sql = "INSERT INTO users (username, email, password,role, created_at, updated_at) \
            VALUES (%s,%s,%s,%s,CURRENT_TIMESTAMP(),CURRENT_TIMESTAMP())"
        cursor.execute(sql, (username, email, password, role))
        database.commit()
        if(cursor.rowcount > 0):
            return True
    except:
        return False


def checkAvailableUsername(value):
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(f"SELECT id FROM users WHERE username = %s ", (value,))
        cursor.fetchone()
        database.commit()
        if(cursor.rowcount > 0):
            return True
        return False
    except:
        return True


def checkAvailableEmail(value):
    try:
        database = connect()
        cursor = database.cursor()
        cursor.execute(f"SELECT id FROM users WHERE email = %s ", (value,))
        cursor.fetchone()
        database.commit()
        if(cursor.rowcount > 0):
            return True
        return False
    except:
        return True


def login(username):
    try:
        database = connect()
        cursor = database.cursor()
        sql = f"SELECT id,password,role,username FROM `users` WHERE username=%s or email =%s"
        cursor.execute(sql, (username, username))
        res = cursor.fetchone()
        database.commit()
        if(cursor.rowcount > 0):
            return {"status": True, "userId": res[0], "username": res[3], "password": res[1], "role": res[2]}
        return {"status": False, "message": "user not found"}
    except:
        return {"status": False, "message": "can't fetch a user"}
