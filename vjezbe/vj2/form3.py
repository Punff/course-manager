#!python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")
formData = cgi.FieldStorage()

print ("Content-type:text/html\r\n\r\n")
print ('''
<html>
<head>
    <title>Forma</title>
</head>
<body>
    <form action="final.py">
        <table border="1">
            <tr>
                <th>Napomena:</th>
                <th>
                    <textarea name="napomena" id="nap" cols="30" rows="10"></textarea>
                </th>
            </tr>
            <tr>
                <th><input type="submit" value="Next"></th>       
            </tr>
        </table>''')
print('<input type="hidden" name="firstname" value="' + str(formData.getvalue("firstname")) + '">')
print('<input type="hidden" name="email" value="' + str(formData.getvalue("email")) + '">')
print('<input type="hidden" name="status" value="' + str(formData.getvalue("status")) + '">')
print('<input type="hidden" name="smjer" value="' + str(formData.getvalue("smjer")) + '">')
if formData.getvalue("zavrsni"):
    print('<input type="hidden" name="zavrsni" value="' + str(formData.getvalue("zavrsni")) + '">')
print('''
    </form>
</body>
</html>
''')
