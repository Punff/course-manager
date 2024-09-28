#!python.exe
import base
import cgi
import cgitb
import session
import years

cgitb.enable(display=0, logdir="")
form = cgi.FieldStorage()

def checked(value, needed):
    return 'checked' if value == needed else ''

session_id = session.get_session_id()
subjects = session.db.get_subjects()
selections = session.db.get_session_data(session_id)
userid = session.db.get_user_id(session_id)
username = session.db.get_username(userid)

for sub in subjects:
    tmp = form.getvalue(sub)
    if tmp is not None:
        selections[sub] = tmp
    elif selections.get(sub) is None:
        selections[sub] = 'Not selected'

session.db.update_session(session_id, selections)

if(form.getvalue("year") == None):
    year = 1
else:
    year = years.year_ids[form.getvalue("year")]

logout = False
if form.getvalue("log_out"):
    logout = True

change_pass = False
if form.getvalue("change_pass"):
    change_pass = True

rows = ''
if form.getvalue("list") is None or form.getvalue("return") is not None:
    for sub in subjects:
        subinfo = subjects[sub]
        if subinfo['year'] == year:
            rows = rows + f'''
            <tr>
                <td>{subinfo['name']}</td>
                <td>{subinfo['ects']}</td>
                <td>
                    <input type="radio" name="{sub}" value="Not selected" {checked(selections[sub], 'Not selected')}> Not selected
                    <input type="radio" name="{sub}" value="Enrolled" {checked(selections[sub], 'Enrolled')}> Enrolled
                    <input type="radio" name="{sub}" value="Passed" {checked(selections[sub], 'Passed')}> Passed
                </td>
            </tr>
            '''

    print("Content-Type: text/html\r\n\r\n")
    base.start_html()
    if logout:
        print('<meta http-equiv="refresh" content="0; url=login.py"/>')
    if change_pass:
        print('<meta http-equiv="refresh" content="0; url=change_password.py"/>')
    print(f'''
        </head><body>
        <h1>Hello {username}</h1>
        <form action="form.py" method="POST">
            <input type="submit" value="1st Year" name="year">
            <input type="submit" value="2nd Year" name="year">
            <input type="submit" value="3rd Year" name="year">
            <table>
                <tr>
                    <th>{years.year_names[year]}</th>
                    <th>Ects</th>
                    <th>Status</th>
                </tr>
                {rows}
            </table>
            <input type="submit" value="List all" name="list">
            <input type="submit" value="Change password" name="change_pass">
            <input type="submit" value="Log out" name="log_out">
        </form>
    ''')
    base.finish_html()

else:
    total = 0
    for sub in subjects:
        subinfo = subjects[sub]
        rows = rows + f'''<tr><td>{subinfo['name']}</td><td>{selections[sub]}</td><td>{subinfo['ects']}</td></tr>'''
        if(selections[sub] == 'Passed'):
            total += subinfo['ects']

    print("Content-Type: text/html\r\n\r\n")
    base.start_html()
    if logout:
        print('<meta http-equiv="refresh" content="0; url=login.py"/>')
    if change_pass:
        print('<meta http-equiv="refresh" content="0; url=change_password.py"/>')
    print(f'''
        </head><body>
        <h1>Hello {username}</h1>
        <form action="form.py" method="POST">
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Status</th>
                    <th>Ects</th>
                </tr>
                {rows}
                <tr>
                    <td></td><td>Total:</td><td>{total}</td>
                </tr>
            </table>
            <input type="submit" value="Back to selection" name="return">
            <input type="submit" value="Change password" name="change_pass">
            <input type="submit" value="Log out" name="log_out">
        </form>
    ''')
    base.finish_html()

