import MPYdata
from MPYdata import *


db=MPYdata()
db.connect('test.db')
db.create_table('test','id int primary key,name text')
db.insert('test',[1,'test1'],[2,'test2'])
db.close()
db.disconnect()