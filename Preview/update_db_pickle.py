import pickle
pickle_f_r = open('people-pickle', 'rb')
db = pickle.load(pickle_f_r)
pickle_f_r.close()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
pickle_f_w = open('people-pickle', 'wb')
pickle.dump(db, pickle_f_w)
pickle_f_w.close()
