bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
tom = dict(name='Tom', age=50, pay=0, job='None')

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
	for person in db.keys():
		print('{} =>\n {}'.format(person, db.get(person)))
