dbfilename = "people-file"
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, db_file_name=dbfilename):
    # test
    fn = open(db_file_name, 'w')
    for key in db:
        print(key, file = fn)
        for (name ,value) in db.get(key).items():
            print('{}=>{}'.format(name, repr(value)), file=fn)
        print(ENDREC, file=fn)
    print(ENDDB, file=fn)
    fn.close()

def loadDbase(db_file_name=dbfilename):
    fn = open(db_file_name, 'r')
    db = {}
    input = ""
    key = fn.readline().strip()
    while key != ENDDB:
        input = fn.readline().strip()
        person = {}
        while input != ENDREC:
            # print("---",input)
            name, value = input.split(RECSEP)
            input = fn.readline().strip()
            person[name] = eval(value)
        db[key] = person
        key = fn.readline().strip()
    return db
    fn.close()

if __name__ == '__main__':
    # from initdata import db
    # storeDbase(db, dbfilename)
    loadDb = loadDbase()
