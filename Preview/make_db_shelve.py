from initdata import bob, sue
import shelve
db = shelve.open('people-shelve')
db['sue'] = sue
db['bob'] = bob
db.close()
