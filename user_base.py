import uuid
import sqlite3


class UsersBase:
    def __init__(self, name="user_base.sqlite"):
        self.con = sqlite3.connect(name, check_same_thread=False)
        self.con.execute('''
        CREATE TABLE IF NOT EXISTS users (
    ip    TEXT,
    id    TEXT,
    name  TEXT,
    admin BLOB,
    dark  BLOB
);
''')
        self.cur = self.con.cursor()

    def get(self, ip, par=None, none=None):
        if par is None:
            arr = self.cur.execute('''SELECT * FROM users
WHERE ip == ?''', (str(ip), )).fetchall()
            if len(arr) == 0:
                return none
            return str(arr[0])
        else:
            arr = self.cur.execute('''SELECT ? FROM users
WHERE ip == ?''', (str(par), str(ip), )).fetchall()
            if len(arr) == 0:
                return none
            return str(arr[0][0])

    def add(self, ip, id, name, admin=False, dark=False):
        self.cur.execute(f'''INSERT INTO users
        VALUES (?, ?, ?, ?, ?)''', (ip, id, name, admin, dark))
        self.con.commit()

    def set(self, ip, par, value):
        self.cur.execute(f'''UPDATE users SET {str(par)} = ?
WHERE ip == ?''', (str(ip), str(value)))
        self.con.commit()


if __name__ == "__main__":
    b = UsersBase()
    # b.add("1", "111", "YOOO")
    # b.set("1", "name", "YOOO")
    print(b.get("1"))
