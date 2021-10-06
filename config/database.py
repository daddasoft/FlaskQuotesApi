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
print(env("host"))
print(env("user"))
print(env("pass"))
print(env("database"))
