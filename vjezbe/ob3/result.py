#! python.exe
import os
import db
import session
import base
import cgi
import cgitb

cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

sessionID = session.getOrCreateSessionID()

data = {}
data["status"] = form.getvalue("status")
data["godina"] = form.getvalue("godina")

db.replaceSession(sessionID, data)
data = db.getSessionData(sessionID)
base.start_html()
for e in data.values():
	print(e)
base.finish_html()
