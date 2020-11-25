from env import env
import mysql.connector


def connect():
    try:
        database = mysql.connector.connect(
            host="containers-us-west-25.railway.app",
            auth_plugin='mysql_native_password',
            port=7361,
            user="root",
            passwd="XKbdczMYhG5b09nPJFaU",
            database="railway"
        )
        return database
    except Exception as ex:
        print(ex)
        return None
print("host : ",env("host"))
print("user : ",env("user"))
print("pass : ",env("pass"))
print("db : ",env("database"))
