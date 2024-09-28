#!python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print  ("""
<!DOCTYPE html>
<html>
<body>
<h2>Unesite podatke:</h2>
<form action="test3.py" method="post">
  Ime:<br>
  <input type="text" name="firstname" value="">
  <br>
  Prezime:<br>
  <input type="text" name="lastname" value="">
  <br><br>
  <input type="submit" value="Submit">
</form> 


</body>
</html>
""")

params = cgi.FieldStorage() 
#print (params)
print (os.environ['REQUEST_METHOD'])
print ("<br>")
if os.environ['REQUEST_METHOD'].upper() == 'POST':
    print (params.getvalue("firstname"))
else:
    print(params.getvalue("lastname"))
