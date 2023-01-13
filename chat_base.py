from user_base import UsersBase
import time
import uuid


class Message:
    user = ""
    time = 0
    id = ""
    user_id = ""
    type = ""
    message = ""

    def __init__(self, user, user_id, time, id, type, message) -> None:
        self.user = user
        self.time = time
        self.id = id
        self.type = type
        self.message = message

    def to_dict(self):
        data = {}
        data["user"] = self.user
        data["time"] = self.time
        data["id"] = self.id
        data["type"] = self.type
        data["message"] = self.message


class ChatBase:
    DELTIME = 3

    def __init__(self, user_base):
        self.user_base: UsersBase = user_base
        self.send_list = []
        self.archive = []

        self.start_time = time.perf_counter()

    def get_time(self):
        return time.perf_counter() - self.start_time()

    def send(self, ip, message, type="message"):
        mes = Message(
            self.user_base(ip), self.user_base[ip], self.get_time(), uuid.uuid1(),
            type, message)
        self.send_list.append(mes)
        self.archive.append(mes)

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
            d = e.to_dict()
            send_chat.append(d)
        return send_chat
