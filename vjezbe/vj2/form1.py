#!python.exe

import cgi
import os
import cgitb
cgitb.enable(display=0, logdir="")

print("Content-type:text/html\r\n\r\n")

print ('''
<html>
<head>
    <title>Forma</title>
</head>
<body>
    <form action="form2.py">
        <table border="1">
            <tr>
                <th>Ime</th>
                <th><input name="firstname" type="text" placeholder="ime"></input></th>
            </tr>
            <tr>
                <th>Lozinka:</th>
                <th><input type="password"></input></th>
            </tr>
            <tr>
                <th>Ponovi lozinku:</th>
                <th><input type="password"></input></th>
            </tr>
            <tr>
                <th><input type="submit" value="Next"></th>
            </tr>
        </table>
    </form>
</body>
</html>
''')