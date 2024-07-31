import sqlite3

class MPYdata:
    def __init__(self):
        self.con = None
        self.cur = None

    def connect(self, dbname):
        if not dbname:
            raise ValueError("Database name cannot be empty")
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()
        return self.cur

    def create_table(self, TableName, values):
        if self.cur:
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {TableName} ({values})")
            self.con.commit()
            return self.cur
        else:
            raise ConnectionError("No active database connection")

    def insert(self, TableName, values):
        if self.cur:
            values_list = values.split(', ')
            placeholders = ', '.join(['?' for _ in values_list])
            self.cur.execute(f"INSERT INTO {TableName} VALUES ({placeholders})", values_list)
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def getall(self, TableName):
        if self.cur:
            self.cur.execute(f"SELECT * FROM {TableName}")
            return self.cur.fetchall()
        else:
            raise ConnectionError("No active database connection")

    def select(self, TableName, valuename):
        if self.cur:
            self.cur.execute(f"SELECT * FROM {TableName} WHERE {valuename}")
            return self.cur.fetchall()
        else:
            raise ConnectionError("No active database connection")

    def delete(self, TableName, valuename):
        if self.cur:
            self.cur.execute(f"DELETE FROM {TableName} WHERE {valuename}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def update(self, TableName, column, value, condition_column, condition_value):
        if self.cur:
            if isinstance(value, str):
                value = f"'{value}'"
            if isinstance(condition_value, str):
                condition_value = f"'{condition_value}'"
            self.cur.execute(f"UPDATE {TableName} SET {column} = {value} WHERE {condition_column} = {condition_value}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def rename_table(self, TableName, NewTableName):
        if self.cur:
            self.cur.execute(f"ALTER TABLE {TableName} RENAME TO {NewTableName}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def delete_table(self, TableName):
        if self.cur:
            self.cur.execute(f"DROP TABLE {TableName}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def create_column(self, TableName, ColumnName, ColumnType):
        if self.cur:
            self.cur.execute(f"ALTER TABLE {TableName} ADD COLUMN {ColumnName} {ColumnType}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")
    
    def rename_column(self, TableName, OldColumnName, NewColumnName):
        if self.cur:
            self.cur.execute(f"ALTER TABLE {TableName} RENAME COLUMN {OldColumnName} TO {NewColumnName}")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def setpassword(self, password):
        if self.cur:
            self.cur.execute(f"PRAGMA rekey = '{password}'")
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def getpassword(self):
        if self.cur:
            self.cur.execute("PRAGMA rekey")
            return self.cur.fetchall()
        else:
            raise ConnectionError("No active database connection")

    def rollback(self):
        if self.con:
            self.con.rollback()
        else:
            raise ConnectionError("No active database connection")

    def close(self):
        if self.con:
            self.con.close()
            self.con = None
            self.cur = None

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def commit(self):
        if self.con:
            self.con.commit()
        else:
            raise ConnectionError("No active database connection")

    def disconnect(self):
        self.close()
    
    def help(self):
        print("This is MPYdata.\n For more help, please visit https://github.com/MahendraYerramsetti/PYdata\n you can also contact 8143418228 ")
