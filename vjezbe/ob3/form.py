#! python.exe
import db
import session
import base

base.start_html()
print(f'''
	<form action="result.py" method="POST">
		<h3>Status</h3>
		<input type="radio" name="status" value="redovni">Redovni
		<input type="radio" name="status" value="izvanredni">Izvanredni
		<h3>Godina</h3>
		<input type="radio" name="godina" value="prva">1
		<input type="radio" name="godina" value="druga">2
		<input type="radio" name="godina" value="treca">3
		<br><br>
		</br>
		<input type="submit" name="submit" value="Submit">
	</form>
''')
base.finish_html()
