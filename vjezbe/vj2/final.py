#! python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

params = cgi.FieldStorage()

print  ("""
<!DOCTYPE html>
<html>
<body>
<form>
        <table border="1">
            <tr style="text-align: center;">
                <td colspan="2" style="font-weight: bold;">Uneseni podaci</td>
            </tr>
            <tr>
                <td>Ime:</td>
            <td>""")
print(str(params.getvalue("firstname")))
print("""</td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td>""")
print(params.getvalue("email"))
print("""</td>
            </tr>
            <tr>
                <td>Studij:</td>
                <td>""")
print(params.getvalue("status"))
print("""</td>
            </tr>
            <tr>
                <td>Smjer:</td>
                <td>""")
print(params.getvalue("smjer"))
print("""</td>
            </tr>
            <tr>
                <td>Zavrsni rad:</td>
                <td>""")
if print(params.getvalue("zavrsni")):
    print(params.getvalue("zavrsni"))
print("""</tr>
            <tr>
                <td>Napomene:</td>
                <td>""")
if print(params.getvalue("napomena")):
    print('<textarea id="napomena" name="napomena" rows="4" cols="50" value="' + str(params.getvalue("napomena")) + '">')
    print(params.getvalue("napomena"))
print("""</textarea>
        </td>
            </tr>
        </table>
        <a href="form1.py">Na pocetak</a>
</form> 
</body>
</html>
""")