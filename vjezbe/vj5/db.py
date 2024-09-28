import mysql.connector
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "vj5",
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

def create_session(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"INSERT INTO sessions (user_id, data) VALUES ({user_id}, '{json.dumps({})}')")
    mydb.commit()
    return cursor.lastrowid

def get_session_user_id(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT user_id FROM sessions WHERE id={session_id}")
    result = cursor.fetchone()
    if result is not None:
        return result[0]
    else:
        return 0
    
def get_session_data(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT data FROM sessions WHERE id={session_id}")
    result = cursor.fetchone()
    if result is not None:
        return json.loads(result[0])
    else:
        return {}

def update_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"""
        UPDATE sessions
        SET data='{json.dumps(data)}'
        WHERE id={session_id}
    """)
    mydb.commit()

def delete_session_db(session_id):
    if session_id is None:
        return
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM sessions WHERE id={session_id}")
    mydb.commit()

def create_user(username, email, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
    usercheck = cursor.fetchone()
    cursor.execute(f"SELECT * FROM users WHERE email='{email}'")
    emailcheck = cursor.fetchone()
    if usercheck is None and emailcheck is None:
        passhash = password_utils.hash_password(password)
        cursor.execute(f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', UNHEX('{passhash.hex()}'))")
        mydb.commit()
        return cursor.lastrowid
    elif usercheck:
        return -1
    else:
        return -2

def get_user(username, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT id, HEX(password) FROM users WHERE username='{username}'")
    result = cursor.fetchone()
    if result is not None:
        if password_utils.verify_password(password, bytes.fromhex(result[1])):
            return result[0]
        else:
            return -1 # Wrong password
    else:
        return -2 # User does not exist

def get_username(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT username FROM users WHERE id={user_id}")
    result = cursor.fetchone()
    return result[0] if result else None

def get_user_id(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT user_id FROM sessions WHERE id={session_id}")
    result = cursor.fetchone()
    return result[0] if result else None

def change_password(user_id, new_password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    passhash = password_utils.hash_password(new_password)
    cursor.execute(f"""
        UPDATE users
        SET password=UNHEX('{passhash.hex()}')
        WHERE id={user_id}
    """)
    mydb.commit()

def get_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    
    cursor.execute(f"SELECT kod, ime, bodovi, godina FROM subjects")
    result = cursor.fetchall()
    subjects = {}
    for el in result:
        subjects[el[0]] = {'name': el[1], 'ects': el[2], 'year': el[3]}
    return subjects
