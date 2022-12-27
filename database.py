import sqlite3
from dataclasses import dataclass, field

# TODO:
#   Comments
#   Database:
#       alter
#       select
#       delete
#       drop
#       rename
#       update
#       -
#       backup
#       describe
#       lock
#       show
#       source
#       status
#       truncate
#       unlock

# Should  be able to be used by people who do not know SQL very well
# Add lamen terms functions

def execute(func):
    def inner(self, *args, **kwargs):

        print("before")
        x = func(self, *args, **kwargs)
        print("after")

        return x
    return inner

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def help(self):
        pass

    def close(self):
        self.connection.close()

    def create_table(self, tablename, **kwargs):
        """
        Creates table in database
        :param tablename: String
        :param kwargs:
        :return: None
        """

        # kwargs can be replaced using functions/variables etc

        # Create fields from kwargs
        fields = ", ".join(names + " " + types for names, types in kwargs.items())

        # Execute MySQL command
        self.cursor.execute(f"CREATE TABLE {tablename} ({fields})")

        # Commit changes and close connection
        self.connection.commit()
        #self.connection.close()

    # Link to something called "add data" or something
    def insert(self, tablename, **kwargs):
        """
        Adds data to table
        :param tablename:
        :param kwargs:
        :return: None
        """

        fields = ", ".join(field for field in kwargs.keys())

        values = ", ".join("'" + value + "'" for value in kwargs.values())

        print(f"INSERT INTO {tablename} ({fields}) VALUES ({values})")

        self.cursor.execute(f"INSERT INTO {tablename} ({fields}) VALUES ({values})")

        self.connection.commit()
        #self.connection.close()

    def delete_table(self, tablename):
        """
        Deletes the specified table
        :param tablename: String
        :return: None
        """
        self.cursor.execute(f"DROP TABLE {tablename}")

        self.connection.commit()
        #self.connection.close()


    # structuring where and select
    # could use inheritance
    # could use decorators
    # first need to figure out proper structure
    # then can use that to figure out which method will work

    @execute
    class Select:
        def __init__(self, *args, **kwargs):

            print("here1")

            self.table = kwargs['tablename']
            self.extracts = ', '.join(args[1:])

            global query
            query = f"SELECT {self.extracts} FROM {self.table}"

        @execute
        class Where:

            def __init__(self, *args, **kwargs):

                fields = list(kwargs.keys())
                values = list(kwargs.values())
                conditions = " AND ".join(str(fields[i]) + "=\'" + str(values[i]) + "\'" for i in range(len(fields)))

                global query
                query += f" WHERE {conditions}"

                print(query)

                #print(f"SELECT {extracts} FROM {table} WHERE {conditions}")







"""
def like(self):
    pass

def match_against(self):
    pass

def limit(self):
    ...

def natural_join(self):
    pass

def join_on(self):
    pass

def join_as(self):
    pass

def group_by(self):
    pass

def order_by(self):
    pass
"""

class Alter:
    """Alters structure of database"""

    # Alter can perform many different commands (index/add/rename/delete etc)

    def rename_table(self):
        pass

    def add_column(self):
        pass

    def rename_column(self):
        pass

    def change_column(self):
        pass

    def drop_column(self):
        pass

    def create_index(self):
        pass

    def create_fulltext(self):
        pass

    def add_primary_key(self):
        pass


class Update:
    def __init__(self):
        pass

    def where(self):
        pass


#  can be called when record is being made
class Record:
    def __init__(self, **fields):
        ...

    def InsertRecord(self, table):

        Database.insert()



# potentially useless - can just translate from default python variables
# can get data type (int, str), then find length and assign to small, medium, long etc
# Can use dataclasses for datatype definitions
class DataType:

    def char(self, n):
        """
        Exactly n (<= 255) bytes
        :param n:
        :return:
        """
        ...

    def varchar(self, n):
        """
        Up to n (<= 65535) bytes
        :param n:
        :return:
        """
        ...

    def binary(self, n):
        """
        Exactly n (<= 255) bytes
        :param n:
        :return:
        """
        ...

    def varbinary(self, n):
        """
        Up to n (<= 65535) bytes
        :param n:
        :return:
        """
        ...

    def tinytext(self, n):
        """
        Exactly n (<= 255) bytes
        :param n:
        :return:
        """
        ...

    def text(self, n):
        """
        Up to n (<= 65535) bytes
        :param n:
        :return:
        """
        ...

    def mediumtext(self, n):
        """
        Up to n (<= 1.67e7) bytes
        :param n:
        :return:
        """
        ...

    def longtext(self, n):
        """
        Up to n (<= 4.29e9) bytes
        :param n:
        :return:
        """
        ...

    def tinyblob(self, n):
        """
        Exactly n (<= 255) bytes
        :param n:
        :return:
        """
        ...

    def blob(self, n):
        """
        Up to n (<= 65535) bytes
        :param n:
        :return:
        """
        ...

    def mediumblob(self, n):
        """
        Up to n (<= 1.67e7) bytes
        :param n:
        :return:
        """
        ...

    def longblob(self, n):
        """
        Up to n (<= 4.29e9) bytes
        :param n:
        :return:
        """
        ...

    def tinyint(self):
        """

        :return:
        """
        ...

    def smallint(self):
        """

        :return:
        """
        ...

    def mediumint(self):
        """

        :return:
        """
        ...

    def integer(self):
        """

        :return:
        """
        ...

    def bigint(self):
        """

        :return:
        """
        ...

    def float(self):
        """

        :return:
        """
        ...

    def double(self):
        """

        :return:
        """
        ...

    def datetime(self):
        """

        :return:
        """
        ...

    def date(self):
        """

        :return:
        """
        ...

    def timestamp(self):
        """

        :return:
        """
        ...

    def time(self):
        """

        :return:
        """
        ...

    def year(self):
        """

        :return:
        """
        ...

    def auto_increment(self):
        """

        :return:
        """
        ...

    def not_null(self):
        """

        :return:
        """
        ...

    def int_unsigned(self):
        """

        :return:
        """
        ...

    def key(self):
        """

        :return:
        """
        ...


if __name__ == "__main__":
    ...
