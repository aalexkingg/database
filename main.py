import database
from database import Database

db_file = r"./db.db"

db = Database(db_file)


#db.create_table('test1', name="varchar(128) not null", id="int")
#db.insert("test1", name="alex", id="301")

db.Select("table1", "var1, var2, var3").where(name="alex", age=19)
