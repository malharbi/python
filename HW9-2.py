# Modify and complet by Motaz Alharbi
#12/02/15
#simple store data user entered into SQLite DB
# PROGRAM 2 in section 9

from wsgiref.simple_server import make_server
import sqlite3

# store data into zooDB database 
def zooDB(animal , count):
	toch = sqlite3.connect("zooDB")
	cursor= toch.cursor()
	try:
		cursor.execute("create table animal_count (name text, count integer)")
	except Exception as e : # to avoid the error if the table already exist 
		pass
	cursor.execute("insert into animal_count(name, count) values(?,?)",(animal, count))
	toch.commit() 
	toch.close() 
	return

# split the data post into wsgi.input
def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	
	zooDB(form_vals['animal'], form_vals['count'])

	return form_vals

def zoo_app(environ, start_response):
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
	message += "<h1>Welcome to the Zoo</h1>"
	message += "<form method='POST'><br>Animal:<input type=text name='animal'>"
	message += "<br><br>Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"
	return[bytes(message,'utf-8')]



httpd = make_server('', 8000, zoo_app)
print("Serving on port 8000...")

httpd.serve_forever()
