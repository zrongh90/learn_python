#! /usr/bin/python3.4
import os
import sys
import shelve
import cgi
form = cgi.FieldStorage()
sys.path.insert(0, '/root/learn_python/Preview')


shelve_name = "/root/learn_python/Preview/class-shelve"


def getPeople(db, form):
    pass


def updatePeople(db, form):
    pass


db = shelve.open(shelve_name)
action = form['action'].value
if action == 'Fetch':
    fields = getPeople(db, form)
elif action == 'Update':
    fields = updatePeople(db, form)
else:
    sys.exit(1)
print(db['bob'])
print(action)
