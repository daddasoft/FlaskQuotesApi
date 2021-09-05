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
    except:
        return None
