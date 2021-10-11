from env import env
import mysql.connector


def connect():
    try:
        database = mysql.connector.connect(
            host=env("remotemysql.com"),
            user=env("8wophxXBD1"),
            passwd=env("G1f5FlqOHS"),
            database=env("8wophxXBD1")
        )
        return database
    except Exception as ex:
        print(ex)
        return None
print("host : ",env("host"))
print("user : ",env("user"))
print("pass : ",env("pass"))
print("db : ",env("database"))
