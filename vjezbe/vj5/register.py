#! python.exe

import base
import cgi
import cgitb
import session

cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

username = form.getvalue("username")
email = form.getvalue("email")
password = form.getvalue("password")
repeat = form.getvalue("repeat")

error = ''
if form.getvalue("submitted"):
    if username is None or email is None or password is None or repeat is None:
        error = 'Missing Values!'
    elif password != repeat:
        error = 'Passwords do not match!'
    else:
        userid = session.db.create_user(username, email, password)
        if userid == -1:
            error = 'An account with that username already exists!'
        elif userid == -2:
            error = 'An account with that email already exists!'


base.start_html()
if form.getvalue("submitted") and error == '':
	print('<meta http-equiv="refresh" content="0; url=login.py"/>')
print(f'''
    </head><body>
      <h2>Register</h2>
      <form action="register.py", method="POST">
        <table>
            <tr><td>Username: </td><td><input type="text" name="username"></td></tr>
            <tr><td>Email: </td><td><input type="email" name="email"></td></tr>
            <tr><td>Password: </td><td><input type="password" name="password"></td></tr>
            <tr><td>Repeat password: </td><td><input type="password" name="repeat"></td></tr>
        </table>
        <br>
        <input type="submit" name="submitted" value="Register"> <a href="login.py">I have an account</a>
      </form>
      <p>{error}</p>

''')
base.finish_html()
