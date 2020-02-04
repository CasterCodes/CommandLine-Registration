import sqlite3 as lite


class User(object):
    def __init__(self):
        global conn
        try:
            conn = lite.connect('users.db')
            with conn:
                cur = conn.cursor()
                sql = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, firstName TEXT, lastName TEXT, email TEXT, password TEXT )"
                cur.execute(sql)
        except Exception:
            print('Error connecting to the databse')

    def inserUserData(self, data):
        try:
            with conn:
                cur = conn.cursor()
                sql = "INSERT INTO  users (firstName, lastName, email,password) VALUES (?,?,?,?)"
                cur.execute(sql, data)
            return True

        except Exception:
            return False

    def selectUser(self, email):
        try:
            with conn:
                cur = conn.cursor()
                sql = "SELECT *  FROM  users WHERE  email = ?"
                cur.execute(sql, email)
                return cur.fetchone()
        except Exception:
            return False

    def selectUsers(self):
        try:
            with conn:
                cur = conn.cursor()
                sql = "SELECT firstName, lastName, email, password FROM  users"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False
