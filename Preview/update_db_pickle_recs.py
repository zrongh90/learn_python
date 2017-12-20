import pickle
sue_file_r = open('sue.pkl', 'rb')
sue = pickle.load(sue_file_r)
sue['pay'] *= 1.1
sue_file_r.close()

sue_file_w = open('sue.pkl', 'wb')
pickle.dump(sue, sue_file_w)
sue_file_w.close()

tom_file_r = open('tom.pkl', 'rb')
tom = pickle.load(tom_file_r)
tom['name'] = "Tom tom"
tom_file_r.close()

tom_file_w = open('tom.pkl', 'wb')
pickle.dump(tom, tom_file_w)
tom_file_w.close()

