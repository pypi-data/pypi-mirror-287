#MPYdata
import sqlite3

class MPYdata:

    def __init__(self):
        self.self = self
    def connect(self, dbname):
        self.dbname = dbname
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        return self.cur

    global values
    def create_table(self,TableName,values):
        self.TableName = TableName
        self.values = values 
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({values}) ")
        self.con.commit()
        self.cur = self.con.cursor()
        return self.cur

    def insert(self, TableName, values):
        values_list = values.split(', ')
        placeholders = ', '.join(['?' for _ in values_list])
        self.cur.execute(f"INSERT INTO {TableName} VALUES ({placeholders})", values_list)
        self.con.commit()

    def getall(self, TableName):
            self.cur.execute(f"SELECT * FROM {TableName}")
            return self.cur.fetchall()
    
    def select(self,TableName,valuename):
        self.TableName = TableName
        self.valuename = valuename
        self.cur.execute(f"SELECT * From {TableName} where {valuename}")
        self.con.commit()
        return self.cur
    
    def delete(self,TableName,valuename):
        self.TableName = TableName
        self.valuename = valuename
        self.cur.execute(f"DELETE FROM {TableName} where {valuename}")
        self.con.commit()
        return self.cur
    
    def update(self, TableName, column, value, condition_column, condition_value):
        # Properly quote string values for SQL
        if isinstance(value, str):
            value = f"'{value}'"
        if isinstance(condition_value, str):
            condition_value = f"'{condition_value}'"
        self.cur.execute(f"UPDATE {TableName} SET {column} = {value} WHERE {condition_column} = {condition_value}")
        self.con.commit()
        return self.cur


    def rename_table(self,TableName,NewTableName):
        self.TableName = TableName
        self.NewTableName = NewTableName
        self.cur.execute(f"ALTER TABLE {TableName} RENAME TO {NewTableName}")
        self.con.commit()
        return self.cur

    def delete_table(self,TableName):
        self.TableName = TableName
        self.cur.execute(f"DROP TABLE {TableName}")
        self.con.commit()
        return self.cur
    
    def rename_column(self,TableName,OldColumnName,NewColumnName):
        self.TableName = TableName
        self.OldColumnName = OldColumnName
        self.NewColumnName = NewColumnName
        self.cur.execute(f"ALTER TABLE {TableName} RENAME COLUMN {OldColumnName} TO {NewColumnName}")
        self.con.commit()
        return self.cur

    def delete_column(self,TableName,ColumnName):
        self.TableName = TableName
        self.ColumnName = ColumnName
        self.cur.execute(f"ALTER TABLE {TableName} DROP COLUMN {ColumnName}")
        self.con.commit()
        return self.cur

    def rename_table(self,TableName,NewTableName):
        self.TableName = TableName
        self.NewTableName = NewTableName
        self.cur.execute(f"ALTER TABLE {TableName} RENAME TO {NewTableName}")
        self.con.commit()
        return self.cur
    def delete_table(self,TableName):
        self.TableName = TableName
        self.cur.execute(f"DROP TABLE {TableName}")
        self.con.commit()
        return self.cur

    def delete(self, TableName, column, value):
        if isinstance(value, str):
            value = f"'{value}'"
        self.cur.execute(f"DELETE FROM {TableName} WHERE {column} = {value}")
        self.conn.commit()
    
    def rollback(self):
        self.con.rollback()
    
    def close(self):
        self.con.close()
    
    def __del__(self):
        try:
            if hasattr(self, 'cur') and self.cur:
                self.cur.close()
                print("Cursor closed.")
            if hasattr(self, 'con') and self.con:
                self.con.close()
                print("Connection closed.")
        except Exception as e:
            print(f"Error during cleanup: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()
    
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

