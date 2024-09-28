import mysql.connector
import json

db_conf = {
    "host":"localhost",
    "db_name": "vj4-2",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def createSession():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"INSERT INTO sessions (data) VALUES ('{json.dumps({})}')")
    mydb.commit()
    return cursor.lastrowid

def getSessionData(sessionID):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT (data) FROM sessions where id={sessionID}")
    data = cursor.fetchone()
    return json.loads(data[0])

def replaceSession(sessionID, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"UPDATE sessions SET data='{json.dumps(data)}' WHERE id={sessionID}")
    mydb.commit()
