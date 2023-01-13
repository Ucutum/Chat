from flask import Flask, request, render_template, abort
from user_base import UsersBase
from chat_base import Chat
import time
import uuid

app = Flask(__name__)

users = UsersBase()
chat = Chat(users)


@app.route("/", methods=["GET", "POST"])
def start():
    return render_template("chat.html")


@app.route("/message", methods=["GET", "POST", "DELETE", "BAN"])
def message():
    global chat

    ip = request.remote_addr
    print(ip)

    if users.get(ip, "black"):
        return {"chat": [{
            "user": "Server", "time": 0, "id": 0, "ip": 0,
            "type": "post", "message": "You was bunned."
            }]}

    if request.method == "POST_MESSAGE":
        data = request.get_json()
        print("data", data)
        chat.send(ip, data.get("message", "message"), "post")
        return {}

    if request.method == "GET_MESSAGE":
        print("GET")
        m = []
        id = users.get(ip, "id")
        for mes in chat.get(ip):
            mes["owner"] = mes["id"] == id
            m.append(mes)
        return {"chat": chat, "admin": users.get(ip, "admin")}

    # if request.method == "DELETE":
    #     if client_ip not in admins:
    #         return abort(403)
    #     data = request.get_json()
    #     print("delete data", data)
    #     data["time"] = time.perf_counter()
    #     data["id"] = uuid.uuid1()
    #     data["ip"] = client_ip
    #     data["type"] = "delete"
    #     chat.append(data)
    #     return {}
    # if request.method == "BAN":
    #     if client_ip not in admins:
    #         return abort(403)
    #     data = request.get_json()

    #     if client_ip == data["ban_ip"]:
    #         return abort(409)

    #     if client_ip in blask_list:
    #         return abort(400)

    #     print("bun user", data)
    #     blask_list.append(data["ban_ip"])

    #     print("data", data)
    #     data["user"] = "Server"
    #     data["message"] = f"Ip {data['ban_ip']} was banned."
    #     data["time"] = time.perf_counter()
    #     data["id"] = uuid.uuid1()
    #     data["ip"] = client_ip
    #     data["type"] = "post"
    #     chat.append(data)

    #     return {}


if __name__ == "__main__":
    # app.run(host="0.0.0.0")
    app.run(debug=True)
