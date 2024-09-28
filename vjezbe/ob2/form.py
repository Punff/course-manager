#!python.exe

import base
import session	
import model
import cgi
import cgitb

cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

base.start_html()	
print('<form action="odabir.py" method="post">')
for key in model.articles:
	article = model.articles[key]
	print(f'''
        <input type="checkbox" name="{article['name']}" value="{article['name']}">{article['name']} {article['price']}<br>''')
        
print('<input type="submit" value="Add"></form>')
base.finish_html()

