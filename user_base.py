import uuid


class UsersBase:
    def __init__(self):
        self.users = {}
        self.black_list = []
        self.admin_list = []

    def random_name(self):
        return "User_" + uuid.uuid1()[:5]

    def get(self, ip):
        if ip in self.users:
            return self.users[ip]
        self.users[ip] = self.random_name()
        return self.get(self, ip)

    def __item__(self, ip):
        self.get(ip)

    def set(self, ip, name=None):
        if name is None:
            name = self.random_name()
        if self.in_base(name=name):
            return
        self.users[ip] = name

    def in_base(self, ip=None, name=None):
        if ip is not None:
            if ip in self.users:
                return True
            else:
                return False
        if name is not None:
            if name in self.users.values():
                return True
            else:
                return False

    def black_add(self, ip):
        if ip in self.black_list:
            return
        self.black_list.append(ip)

    def black_remove(self, ip):
        if ip not in self.black_list:
            return
        self.black_list.remove(ip)

    def is_black(self, ip):
        return ip in self.black_list

    def admin_add(self, ip):
        if ip in self.admin_list:
            return
        self.admin_list.append(ip)

    def admin_remove(self, ip):
        if ip not in self.admin_list:
            return
        self.admin_list.remove(ip)

    def is_admin(self, ip):
        return ip in self.admin_list
