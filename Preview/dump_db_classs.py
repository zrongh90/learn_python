import shelve
db = shelve.open("class-shelve")
for key in db:
    print("{} =>\n {} {}".format(key, db[key].name, db[key].pay))
db.close()
