import shelve
import random

db = shelve.open('test')
# data = {'first' : 'asdf', 'second' : 'balabala', 'third' : '233333333'}
# for x in data:
#     db[x] = data[x]

print(len(db))
print(db.keys())

for key in db:
    print(db[key])
    db[key] = ''.join(random.sample('!@#$%^&*()_+-<>/,.{}[]\|;"\':~`QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456879',5))

for key in db:
    print(db[key])

db.close()