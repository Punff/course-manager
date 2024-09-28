import db
import os
from http import cookies

def get_session_id():
    cookies_object = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
    return cookies_object.get("session_id").value if cookies_object.get("session_id") else None

def create_session(user_id):
    session_id = get_session_id()
    if session_id is None:
        session_id = db.create_session(user_id)
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output())
    return session_id


def delete_session():
    session_id = get_session_id()
    cookies_object = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
    cookies_object["session_id"] = None
    cookies_object["session_id"]["expires"] = 0
    print(cookies_object.output())
    db.delete_session_db(session_id)
