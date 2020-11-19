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
