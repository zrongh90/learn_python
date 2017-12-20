import pickle, glob
for filename in glob.glob('*.pkl'):
    rec_file = open(filename, 'rb')
    record = pickle.load(rec_file)
    print(filename, '=>\n', record)

sue_file = open('sue.pkl', 'rb')
sue = pickle.load(sue_file)
print(sue['name'])
