#! python.exe

import cgi
import os
import cgitb
import subjects
from http import cookies

def bake(cookie):
    print(cookie)

cgitb.enable(display=0, logdir=".")
form = cgi.FieldStorage()

if(form.getvalue("year") == None):
    year = 1
else:
    year = subjects.year_ids[form.getvalue("year")]

prevYear = form.getvalue("previous")

cookie_string = os.environ.get('HTTP_COOKIE', '')
cookie = cookies.SimpleCookie()
if cookie_string:
    cookie.load(cookie_string)

if prevYear:
    for sub, subInfo in subjects.subjects.items():
        if int(subInfo["year"]) == int(prevYear):
            status = form.getvalue(subInfo['name'])
            cookie[sub] = status if status else "Not selected"
    bake(cookie)

selections = []
for sub in subjects.subjects:
    subInfo = subjects.subjects[sub]
    if subInfo["year"] == year:
        tmp = cookie.get(sub)
        status = tmp.value if tmp else "Not selected"
        sel = {
            'name': subInfo['name'],
            'ects': subInfo['ects'],
            'value': status
        }
        selections.append(sel)
    

def checked(value, needed):
    return 'checked' if value == needed else ''

tableRows = ''
for sel in selections:
    tableRows += f'''
    <tr>
        <td>{sel['name']}</td>
        <td>{sel['ects']}</td>
        <td>
            <input type=radio name="{sel['name']}" value="Enrolled" {checked(sel['value'], 'Enrolled')}>Enrolled
            <input type=radio name="{sel['name']}" value="Not selected" {checked(sel['value'], 'Not selected')}>Not selected
            <input type=radio name="{sel['name']}" value="Passed" {checked(sel['value'], 'Passed')}>Passed
        </td>
    </tr>
    '''

# HTML
print("Content-Type: text/html\r\n\r\n")
# Header
print(f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Selection</title>
    <style>
        table {{ border: 1px solid grey; border-collapse: collapse; }}
        table caption {{ padding: 8px; }}
        table th, table td {{ padding: 8px; border: 1px solid lightgrey; }}
    </style>
</head>''')


# Body
print(f'''
<body>
    <form>
        <input type="hidden" value="{year}" name="previous">
        <input type=submit value="1st Year" name="year">
        <input type=submit value="2nd Year" name="year">
        <input type=submit value="3rd Year" name="year">
        <table>
            <tr>
                <th>{subjects.year_names[year]}</th>
                <th>ECTS</th>
                <th>Status</th>
                {tableRows}
            </tr>
        </table>
    </form>
        <a href="list.py">List all</a>
</body>
</html>
'''
)
