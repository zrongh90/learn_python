from initdata import tom
import shelve
db = shelve.open('people-shelve')
db['tom'] = tom
sue = db['sue']
sue['pay'] *= 1.1
db['sue'] = sue
db.close()
