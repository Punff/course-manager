#!python.exe

import cgi
params = cgi.FieldStorage()
#first_name = params.getvalue("firstname")

print ('''
<!DOCTYPE html>
<html>
<body>

<h2>Odaberite smjer:</h2>

<form action="test4.py" method="post">
  <select name="smjer_studija">
    <option value="programiranje">programiranje</option>
    <option value="baze_podataka">baze podataka</option>
    <option value="mreze">mreze</option>
    <option value="informacijski_sustavi">informacijski sustavi</option>
  </select>
  <br><br>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')
print ('''
<br>
<input type="submit" value="submit">
</form>

</body>
</html>''')
print("Ovako se zovu post parametri iz skripte koja se submit-ala na test3.py: ")
print (params.getvalue("firstname"))
print ('<br>')
print("Parametri pod ovim imenom ne postoje: ")
print (params.getvalue("ime"))
