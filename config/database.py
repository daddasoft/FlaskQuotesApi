from env import env
import mysql.connector


def connect():
    try:
        database = mysql.connector.connect(
            host=env("host"),
            user=env("user"),
            passwd=env("pass"),
            database=env("database")
        )
        return database
    except Exception as ex:
        print(ex)
        return None
print("host : ",env("host"))
print("user : ",env("user"))
print("pass : ",env("pass"))
print("db : ",env("database"))
