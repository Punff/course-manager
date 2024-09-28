#! python.exe

import base
import cgi
import model
import cgitb
import session

cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

sessionid = session.get_or_create_session_id()

result = {}
for key in model.articles:
    article = model.articles[key]
    if form.getvalue(f"{article['name']}"):
        result[key] = article['name']

session.add_to_session(result, sessionid)

data = session.db.get_session(sessionid)

base.start_html()
for i in model.articles:
	for j in data:
		if int(i) == int(j):
			print(model.articles[i]['name'])
base.finish_html()

