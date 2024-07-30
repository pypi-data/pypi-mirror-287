#MPYdata
#Mahendra Sai Phaneeswar Yerramsetti
#https://github.com/MahendraYerramsetti/PYdata

import sqlite3

class MPYdata:
    def __init__(self):
        self.con = None
        self.cur = None

    def connect(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        return self.cur

    def create_table(self, TableName, values):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({values})")
        self.con.commit()
        return self.cur

    def insert(self, TableName, values):
        values_list = values.split(', ')
        placeholders = ', '.join(['?' for _ in values_list])
        self.cur.execute(f"INSERT INTO {TableName} VALUES ({placeholders})", values_list)
        self.con.commit()

    def getall(self, TableName):
        self.cur.execute(f"SELECT * FROM {TableName}")
        return self.cur.fetchall()

    def select(self, TableName, valuename):
        self.cur.execute(f"SELECT * FROM {TableName} WHERE {valuename}")
        return self.cur.fetchall()

    def delete(self, TableName, valuename):
        self.cur.execute(f"DELETE FROM {TableName} WHERE {valuename}")
        self.con.commit()

    def update(self, TableName, column, value, condition_column, condition_value):
        if isinstance(value, str):
            value = f"'{value}'"
        if isinstance(condition_value, str):
            condition_value = f"'{condition_value}'"
        self.cur.execute(f"UPDATE {TableName} SET {column} = {value} WHERE {condition_column} = {condition_value}")
        self.con.commit()

    def rename_table(self, TableName, NewTableName):
        self.cur.execute(f"ALTER TABLE {TableName} RENAME TO {NewTableName}")
        self.con.commit()

    def delete_table(self, TableName):
        self.cur.execute(f"DROP TABLE {TableName}")
        self.con.commit()

    def create_column(self, TableName, ColumnName, ColumnType):
        self.cur.execute(f"ALTER TABLE {TableName} ADD COLUMN {ColumnName} {ColumnType}")
        self.con.commit()
    
    def drop_column(self, TableName, ColumnName):
        self.cur.execute(f"ALTER TABLE {TableName} DROP COLUMN {ColumnName}")
        self.con.commit()
    
    def setpassword(self, password):
        self.cur.execute(f"PRAGMA rekey = '{password}'")
        self.con.commit()

    def getpassword(self):
        self.cur.execute("PRAGMA rekey")
        return self.cur.fetchall()

    def dbname(self):
        return self.dbname

    def colapsdb(self):
        return self.con

    def delete_column(self, TableName, ColumnName):
        self.cur.execute(f"ALTER TABLE {TableName} DROP COLUMN {ColumnName}")
        self.con.commit()
    
    def rename_column(self, TableName, OldColumnName, NewColumnName):
        self.cur.execute(f"ALTER TABLE {TableName} RENAME COLUMN {OldColumnName} TO {NewColumnName}")
        self.con.commit()

    def rollback(self):
        self.con.rollback()

    def close(self):
        if self.con:
            self.con.close()

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def showalldata(self):
        print(self.cur.fetchall())

    def showallcolumns(self):
        print(self.cur.description)

    def showalltables(self):
        print(self.cur.fetchall())

    def showallvalues(self):
        print(self.cur.fetchall())

    def showalltypes(self):
        print(type(self.cur.fetchall()))

    def commit(self):
        self.con.commit()

    def disconnect(self):
        self.con.close()
    
    def help(self):
        print("This is MPYdata.\n For more help, please visit https://github.com/MahendraYerramsetti/PYdata\n you can also contact 8143418228 ")
        