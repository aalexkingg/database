import database
from database import Database, DataType

db = Database('root', '', 'localhost', 'python')

#db.create_table('test2', name="varchar(128) not null", id="int")
#db.insert("test1", name="alex", id="301")

database.select("test1", "extract").where(name="name")
db.select().where()
