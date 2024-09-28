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
    <form action="form3.py">
        <table border="1">
            <tr>
                <th>Status:</th>
                <th>
                    <input type="radio" name="status" value="red">Redovan</input>
                    <input type="radio" name="status" value="izv">Izvanredan</input>
                </th>
            </tr>
            <tr>
                <th>Email:</th>
                <th>
                    <input name="email" type="email" placeholder="primjer@primjer.com"></input>
                </th>
            </tr>
            <tr>
                <th>Smjer:</th>
                <th>
                    <select name="smjer" id="smjer">
                        <option value="BP">Baze Podataka</option>
                        <option value="RM">Racunalne Mreze</option>
                        <option value="WEB">Web Programiranje</option>
                      </select> 
                </th>
            </tr>
            <tr>
                <th>Završni:</th>
                <th>
                    <input name="zavrsni" type="checkbox">
                </th>
            </tr>
            <tr>
                <th><input type="submit" value="Next"></th>       
            </tr>
        </table>''')
print('<input type="hidden" name="firstname" value="' + str(formData.getvalue("firstname")) + '">')
print('''
    </form>
</body>
</html>
''')