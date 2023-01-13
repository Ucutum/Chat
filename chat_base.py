from user_base import UsersBase
import time
import uuid
import sqlite3


class Message:
    user = ""
    time = 0
    id = ""
    user_id = ""
    type = ""
    message = ""


class ArchiveBase:
    def __init__(self, name="user_base.sqlite", check_same_thread=False):
        self.con = sqlite3.connect(name)
        self.con.execute('''
        CREATE TABLE IF NOT EXISTS archive (
    user    TEXT,
    time    TEXT,
    id  TEXT,
    user_id TECT,
    type  TEXT,
    message TEXT
);
''')
        self.cur = self.con.cursor()

    def random_user(self):
        return ("User_" + uuid.uuid1()[:5], uuid.uuid1())

    def get(self, ip, par=None, none=None):
        if par is None:
            arr = self.cur.execute('''SELECT * FROM archive
WHERE ip == ?''', (str(ip), )).fetchall()
            if len(arr) == 0:
                return none
            return str(arr[0])
        else:
            arr = self.cur.execute('''SELECT ? FROM archive
WHERE ip == ?''', (str(par), str(ip), )).fetchall()
            if len(arr) == 0:
                return none
            return str(arr[0][0])

    def add(self, user, time, id, user_id, type, message):
        self.cur.execute(f'''INSERT INTO archive
        VALUES (?, ?, ?, ?, ?, ?)''', (user, time, id, user_id, type, message))
        self.con.commit()

    def set(self, ip, par, value):
        self.cur.execute(f'''UPDATE archive SET {str(par)} = ?
WHERE ip == ?''', (str(ip), str(value)))
        self.con.commit()


class Chat:
    DELTIME = 3

    def __init__(self, user_base):
        self.user_base: UsersBase = user_base
        self.send_list = []
        self.archive = ArchiveBase()

        self.start_time = time.perf_counter()

    def get_time(self):
        return time.perf_counter() - self.start_time()

    def send(self, ip, message, type="message"):
        t = self.get_time()
        id = uuid.uuid1()
        mes = {
            "user": self.user_base.get(ip, "name"),
            "time": t,
            "id": id,
            "user_id": self.user_base.get(ip, "id"),
            "type": type,
            "message": message
            }
        self.send_list.append(mes)
        self.archive.add(
            self.user_base.get(ip, "name"),
            t, id, self.user_base.get(ip, "id"),
            type, message
        )

    def update(self):
        i = 0
        while i < len(self.send_list):
            mes = self.send_list[i]
            if self.get_time() - mes.time >= self.DELTIME:
                del self.send_list[i]
                i -= 1
            i += 1

    def get(self, ip):
        send_chat: list[Message] = []
        for e in self.send_list:
            send_chat.append(e)
        return send_chat
