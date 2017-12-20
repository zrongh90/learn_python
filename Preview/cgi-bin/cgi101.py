#!/usr/bin/python3.4
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title> Reply Page </title>')
if not 'user' in form:
    print('<h1> who are you?</h1>')
else:
    print('<h1>Hello <i>{}</i></h1>'.format(cgi.escape(form['user'].value)))
    # print('<h1>Hello <i></i></h1>')
