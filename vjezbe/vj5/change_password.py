#!python.exe

import base
import cgi
import cgitb
cgitb.enable(display=0, logdir="")
import session
form = cgi.FieldStorage()

error_msg = ''

session_id = session.get_session_id()

password = form.getvalue("password")
newp = form.getvalue("new_password")
repeat = form.getvalue("repeat")
userid = session.db.get_user_id(session_id)
username = session.db.get_username(userid)

success = False
if form.getvalue("submitted"):
    if password is None or newp is None or repeat is None:
        error_msg = 'Missing values'
    elif newp == repeat:
        userid = session.db.get_user(username, password)
        if userid == -1:
            error_msg = 'Wrong password!'
        else:
            session.db.change_password(session.db.get_user_id(session_id), newp)
            success = True
    else:
        error_msg = 'Passwords do not match!'

base.start_html()
if success:
    print('<meta http-equiv="refresh" content="0; url=login.py"/>')
print(f'''
    </head><body>
      <h2>Change password</h2>
      <form action="change_password.py", method="POST">
        <input type="hidden" name="submitted" value="1">
        <table>
            <tr><td>Password: </td><td><input type="password" name="password"></td></tr>
            <tr><td>New password: </td><td><input type="password" name="new_password"></td></tr>
            <tr><td>Repeat new password: </td><td><input type="password" name="repeat"></td></tr>
        </table>
        <br>
        <input type="submit" name="submitted" value="Change"> <a href="login.py">Login</a>
        <p>{error_msg}</p>
      </form>
    </body></html>
''')
