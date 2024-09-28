import db
import os
from http import cookies

def get_or_create_session_id():
    cookieStr = os.environ.get("HTTP_COOKIE", "")
    allCookies = cookies.SimpleCookie(cookieStr)
    sessionID = allCookies.get("sessionID").value if allCookies.get("sessionID").value else None
    if sessionID is None:
        sessionID = db.create_session()
        cookieobject = cookies.SimpleCookie()
        cookieobject["sessionID"] = session_id
        print(cookieObject.output())
    return sessionID

