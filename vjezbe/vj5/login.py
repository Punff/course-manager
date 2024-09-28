#! python.exe

import base
import cgi
import cgitb
import session
cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

session.delete_session()

username = form.getvalue("username")
password = form.getvalue("password")

error = ''
if form.getvalue("submitted"):
    if username is None or password is None:
        error = 'Missing values!'
    else:
        userid = session.db.get_user(username, password)
        if userid == -1:
            error = 'Wrong password!'
        elif userid == -2:
            error = 'User does not exist!'
        else:
            session.create_session(userid)

base.start_html()
if form.getvalue("submitted") and error == '':
    print('<meta http-equiv="refresh" content="0; url=form.py"/>')
print(f'''
    </head><body>
      <h2>Login</h2>
      <form action="login.py" method="POST">
        <input type="hidden" name="submitted" value="1">
        <table>
            <tr><td>Username: </td><td><input type="text" name="username"></td></tr>
            <tr><td>Password: </td><td><input type="password" name="password"></td></tr>
        </table>
        <br>
        <input type="submit" name="submitted" value="Login"> <a href="register.py">Create an account</a>
        <p>{error}</p>
      </form>
''')
base.finish_html()

