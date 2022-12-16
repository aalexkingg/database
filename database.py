import mysql.connector

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


class Database:
    def __init__(self, user, password, host, database):
        self.connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.connection.cursor()

    def create_table(self, tablename, **kwargs):
        """
        Creates table in database
        :param tablename: String
        :param kwargs:
        :return: None
        """
        # Create fields from kwargs
        fields = ", ".join(names + " " + types for names, types in kwargs.items())

        # Execute MySQL command
        self.cursor.execute(f"CREATE TABLE {tablename} ({fields})")

        # Commit changes and close connection
        self.connection.commit()
        self.connection.close()

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
        self.connection.close()

    def delete_table(self, tablename):
        """
        Deletes the specified table
        :param tablename: String
        :return: None
        """
        self.cursor.execute(f"DROP TABLE {tablename}")

        self.connection.commit()
        self.connection.close()

    def select(self, tablename, extract):
        def __init__(self, tablename, extract):
            self.tablename = tablename
            self.extract = extract

        def where(self, **kwargs):
            print(f"{self.tablename} and {self.extract} and {kwargs}")

        def like(self):
            pass

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

        def match_against(self):
            pass

        def limit(self):
            pass

    def alter(self):
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

    def update(self):
        def __init__(self):
            pass

        def where(self):
            pass


class select:
    def __init__(self, tablename, extract):
        self.tablename = tablename
        self.extract = extract

    def where(self, **kwargs):
        print(f"{self.tablename} and {self.extract} and {kwargs}")

    def like(self):
        pass

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

    def match_against(self):
        pass

    def limit(self):
        pass


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

# TODO:
#   Record:
#       -

class Record:

    def __init__(self, **fields):

        self.activityID = fields['ActivityID']
        self.moduleName = fields['ModuleName']
        self.completionState = fields['CompletionState']
        self.weekNumber = fields['WeekNumber']
        self.courseID = fields['CourseID']
        self.sectionID = fields['SectionID']
        self.deadline = fields['Deadline']
        self.activityType = fields['ActivityType']

    def InsertRecord(self, table):

        __insert__(table = table,
                    activityID = self.activityID,
                    moduleName = self.moduleName,
                    completionState = self.completionState,
                    weekNumber = self.weekNumber,
                    courseID = self.courseID,
                    sectionID = self.sectionID,
                    deadline = self.deadline,
                    activityType = self.activityType)

# TODO:
#   DataType:
#       char(n)
#       varchar(n)
#       -
#       binary(n)/byte(n)
#       varbinary(n)
#       -
#       tinytext(n)
#       text(n)
#       mediumtext(n)
#       longtext(n)
#       -
#       tinyblob(n)
#       blob(n)
#       mediumblob(n)
#       longblob(n)
#       -
#       tinyint
#       smallint
#       mediumint
#       int
#       bigint
#       float
#       double/real
#       -
#       datetime
#       date
#       timestamp
#       time
#       year
#       -
#       autoincrement
#       not null
#       unsigned
#       key

class DataType:
    pass