import shelve
from person import Person
from manager import Manager

bob = Person(name='Bob Smith', age=42, pay=30000, job='software')
sue = Person(name='Sue Johns', age=45, pay=40000, job='hardware')
tom = Manager(name='Tom Doe', age=50, pay=50000)
db = shelve.open("class-shelve")
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
