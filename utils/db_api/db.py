import sqlite3
from sqlite3 import Error

class Database():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create_table_users(self):
        sql = """CREATE TABLE IF NOT EXISTS users 
                (id INTEGER NOT NULL,
                user_id INTEGER NOT NULL UNIQUE,
                full_name TEXT,
                PRIMARY KEY("id")
                );"""
        
        self.execute(sql)

    def execute(self, sql):
        with self.connection:
            return self.cursor.execute(sql)

    def user_exists(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM users where user_id = ?", (user_id,)).fetchall()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users ('user_id') VALUES(?)", (user_id,))
        
    def add_fullname(self, user_id, full_name):
        with self.connection:
            sql = """
            INSERT INTO users ('user_id', 'full_name') 
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET full_name = excluded.full_name
            """
        return self.cursor.execute(sql, (user_id, full_name))
           