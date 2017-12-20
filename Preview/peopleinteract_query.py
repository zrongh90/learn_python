import shelve
fieldnames = ['name', 'age', 'pay', 'job']
maxfield = max(len(f) for f in fieldnames)
db = shelve.open("class-shelve")

while True:
    key = input('\nKey? => ')
    if not key: break
    try:
        record = db[key]
        for field in fieldnames:
            print("{} => {}".format(field.ljust(maxfield), getattr(record, field)))
    except:
        print("No such key \"{}\"".format(key))
db.close()
