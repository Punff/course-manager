import json
import db
import os
from http import cookies

def getOrCreateSessionID():
    cookieStr = os.environ.get("HTTP_COOKIE", "")
    allCookies = cookies.SimpleCookie(cookieStr)
    sessionID = allCookies.get("sessionID").value if allCookies.get("sessionID") else None
    if sessionID is None:
        sessionID = db.createSession()
        cookieObject = cookies.SimpleCookie()
        cookieObject["sessionID"] = sessionID
        print(cookieObject.output())
    return sessionID
