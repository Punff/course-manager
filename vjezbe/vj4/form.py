#!python.exe

import base
import cgi
import subjects
import cgitb
import session

cgitb.enable(display=0, logdir="")
field_storage = cgi.FieldStorage()

def checked(value, needed):
    return 'checked' if value == needed else ''

session_id = session.get_or_create_session_id()
selections = session.db.get_session(session_id)

for sub in subjects.subjects:
    tmp = field_storage.getvalue(sub)
    if tmp is not None:
        selections[sub] = tmp
    elif selections.get(sub) is None:
        selections[sub] = 'Not selected'

session.add_to_session(selections)

if(field_storage.getvalue("year") == None):
    year = 1
else:
    year = subjects.year_ids[field_storage.getvalue("year")]


rows = ''
if field_storage.getvalue("list") is None or field_storage.getvalue("return") is not None:
    for sub in subjects.subjects:
        subinfo = subjects.subjects[sub]
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
    print('''
        <form action="form.py" method="POST">
            <input type="submit" value="1st Year" name="year">
            <input type="submit" value="2nd Year" name="year">
            <input type="submit" value="3rd Year" name="year">
            <table>
                <tr>
                    <th>''' + str(subjects.year_names[year]) + '''</th>
                    <th>Ects</th>
                    <th>Status</th>
                </tr>''' + rows + '''
            </table>
            <input type="submit" value="List all" name="list">
        </form>''')
    base.finish_html()

else:
    total = 0
    for sub in subjects.subjects:
        subinfo = subjects.subjects[sub]
        rows = rows + f'''<tr><td>{subinfo['name']}</td><td>{selections[sub]}</td><td>{subinfo['ects']}</td></tr>'''
        if(selections[sub] == 'Passed'):
            total += subinfo['ects']

    print("Content-Type: text/html\r\n\r\n")
    base.start_html()
    print(f'''
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
        </form>
    ''')
    
    base.finish_html()

